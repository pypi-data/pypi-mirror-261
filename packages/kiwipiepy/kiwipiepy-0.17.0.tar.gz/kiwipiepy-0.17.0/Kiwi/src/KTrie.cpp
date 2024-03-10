#include <numeric>
#include <kiwi/Types.h>
#include <kiwi/TemplateUtils.hpp>
#include <kiwi/Utils.h>
#include "ArchAvailable.h"
#include "KTrie.h"
#include "FeatureTestor.h"
#include "FrozenTrie.hpp"

using namespace std;
using namespace kiwi;

namespace kiwi
{
	template<class... Args>
	inline bool appendNewNode(Vector<KGraphNode>& nodes, Vector<pair<uint32_t, uint32_t>>& endPosMap, size_t startPos, Args&&... args)
	{
		static constexpr uint32_t npos = -1;

		if (endPosMap[startPos].first == endPosMap[startPos].second)
		{
			return false;
		}

		size_t newId = nodes.size();
		nodes.emplace_back(forward<Args>(args)...);
		auto& nnode = nodes.back();
		nnode.startPos = startPos;

		nnode.prev = newId - endPosMap[startPos].first;
		if (nnode.endPos >= endPosMap.size()) return true;

		if (endPosMap[nnode.endPos].first == endPosMap[nnode.endPos].second)
		{
			endPosMap[nnode.endPos].first = newId;
			endPosMap[nnode.endPos].second = newId + 1;
		}
		else
		{
			nodes[endPosMap[nnode.endPos].second - 1].sibling = newId - (endPosMap[nnode.endPos].second - 1);
			endPosMap[nnode.endPos].second = newId + 1;
		}
		return true;
	}

	struct TypoCostInfo
	{
		float cost;
		uint32_t start;
		uint32_t typoId;

		TypoCostInfo(float _cost = 0, uint32_t _start = 0, uint32_t _typoId = 0)
			: cost{ _cost }, start{ _start }, typoId{ _typoId }
		{}
	};

	template<bool typoTolerant>
	bool getZCodaAppendable(
		const Form* foundCand,
		const Form* formBase
	)
	{
		if (typoTolerant)
		{
			auto tCand = reinterpret_cast<const TypoForm*>(foundCand);
			return tCand->form(formBase).zCodaAppendable;
		}
		else
		{
			return foundCand->zCodaAppendable;
		}
	}

	template<bool typoTolerant>
	bool insertCandidates(
		Vector<const Form*>& candidates,
		Vector<TypoCostInfo>& candTypoCostStarts,
		const Form* foundCand,
		const Form* formBase,
		const size_t* typoPtrs,
		U16StringView str,
		const Vector<uint32_t>& nonSpaces
	)
	{
		if (typoTolerant)
		{
			auto tCand = reinterpret_cast<const TypoForm*>(foundCand);
			if (find(candidates.begin(), candidates.end(), &tCand->form(formBase)) != candidates.end()) return false;

			while (1)
			{
				auto typoFormSize = typoPtrs[tCand->typoId + 1] - typoPtrs[tCand->typoId];
				auto cand = &tCand->form(formBase);
				if (FeatureTestor::isMatched(&str[0], &str[nonSpaces[nonSpaces.size() - typoFormSize]], tCand->leftCond)
					&& FeatureTestor::isMatchedApprox(&str[0], &str[nonSpaces[nonSpaces.size() - typoFormSize]], cand->vowel, cand->polar))
				{
					candidates.emplace_back(cand);
					candTypoCostStarts.emplace_back(tCand->score(), nonSpaces.size() - typoFormSize, tCand->typoId);
				}
				if (tCand[0].hash() != tCand[1].hash()) break;
				++tCand;
			}
		}
		else
		{
			if (find(candidates.begin(), candidates.end(), foundCand) != candidates.end()) return false;

			while (1)
			{
				if (FeatureTestor::isMatchedApprox(&str[0], &str[nonSpaces[nonSpaces.size() - foundCand->form.size()]], foundCand->vowel, foundCand->polar))
				{
					candidates.emplace_back(foundCand);
				}
				if (foundCand[0].formHash != foundCand[1].formHash) break;
				++foundCand;
			}
		}
		return true;
	}

	inline void removeUnconnected(Vector<KGraphNode>& ret, const Vector<KGraphNode>& graph, const Vector<std::pair<uint32_t, uint32_t>>& endPosMap)
	{
		thread_local Vector<uint8_t> connectedList;
		thread_local Vector<uint16_t> newIndexDiff;		
		thread_local Deque<uint32_t> updateList;
		connectedList.clear();
		connectedList.resize(graph.size());
		newIndexDiff.clear();
		newIndexDiff.resize(graph.size());
		updateList.clear();
		updateList.emplace_back(graph.size() - 1);
		connectedList[graph.size() - 1] = 1;

		while (!updateList.empty())
		{
			const auto id = updateList.front();
			updateList.pop_front();
			const auto& node = graph[id];
			const auto scanStart = endPosMap[node.startPos].first, scanEnd = endPosMap[node.startPos].second;
			for (auto i = scanStart; i < scanEnd; ++i)
			{
				if (graph[i].endPos != node.startPos) continue;
				if (connectedList[i]) continue;
				updateList.emplace_back(i);
			}
			fill(connectedList.begin() + scanStart, connectedList.begin() + scanEnd, 1);
		}

		size_t connectedCnt = accumulate(connectedList.begin(), connectedList.end(), 0);
		newIndexDiff[0] = connectedList[0];
		for (size_t i = 1; i < graph.size(); ++i)
		{
			newIndexDiff[i] = newIndexDiff[i - 1] + connectedList[i];
		}
		for (size_t i = 0; i < graph.size(); ++i)
		{
			newIndexDiff[i] = i + 1 - newIndexDiff[i];
		}

		ret.reserve(connectedCnt);
		for (size_t i = 0; i < graph.size(); ++i)
		{
			if (!connectedList[i]) continue;
			ret.emplace_back(graph[i]);
			auto& newNode = ret.back();
			if (newNode.prev) newNode.prev -= newIndexDiff[i] - newIndexDiff[i - newNode.prev];
			if (newNode.sibling)
			{
				if (connectedList[i + newNode.sibling]) newNode.sibling -= newIndexDiff[i + newNode.sibling] - newIndexDiff[i];
				else newNode.sibling = 0;
			}
		}
	}

}

// nonSpaces idx 데이터로부터 글자 수 + 공백 블록 수를 계산한다.
template<class It>
inline size_t countChrWithNormalizedSpace(It first, It last)
{
	size_t n = std::distance(first, last);
	auto prevIdx = *first++;
	for (; first != last; ++first)
	{
		if (*first != prevIdx + 1) ++n;
		prevIdx = *first;
	}
	return n;
}

// 공백 문자의 위치가 형태소의 공백 위치와 불일치하는 개수를 센다.
inline size_t countSpaceErrors(const KString& form, const uint32_t* spaceIdxFirst, const uint32_t* spaceIdxLast)
{
	size_t n = 0;
	size_t spaceOffset = 0;
	const size_t size = std::distance(spaceIdxFirst, spaceIdxLast);
	for (size_t i = 1; i < size; ++i)
	{
		const bool hasSpace = spaceIdxFirst[i] - spaceIdxFirst[i - 1] > 1;
		if (hasSpace && form[i + spaceOffset] != u' ') ++n;
		spaceOffset += form[i + spaceOffset] == u' ' ? 1 : 0;
	}
	return n;
}

template<ArchType arch, bool typoTolerant>
size_t kiwi::splitByTrie(
	Vector<KGraphNode>& ret,
	const Form* formBase,
	const size_t* typoPtrs,
	const utils::FrozenTrie<kchar_t, const Form*>& trie, 
	U16StringView str,
	size_t startOffset,
	Match matchOptions, 
	size_t maxUnkFormSize, 
	size_t spaceTolerance,
	float typoCostWeight,
	const PretokenizedSpanGroup::Span*& pretokenizedFirst,
	const PretokenizedSpanGroup::Span* pretokenizedLast
)
{
	/*
	* endPosMap[i]에는 out[x].endPos == i를 만족하는 첫번째 x(first)와 마지막 x + 1(second)가 들어 있다.
	* first == second인 경우 endPos가 i인 노드가 없다는 것을 의미한다.
	* first <= x && x < second인 out[x] 중에는 endPos가 i가 아닌 것도 있을 수 있으므로 주의해야 한다.
	*/
	thread_local Vector<pair<uint32_t, uint32_t>> endPosMap;
	endPosMap.clear();
	endPosMap.resize(str.size() + 1, make_pair<uint32_t, uint32_t>(-1, -1));
	endPosMap[0] = make_pair(0, 1);
	
	thread_local Vector<uint32_t> nonSpaces;
	nonSpaces.clear();
	nonSpaces.reserve(str.size());

	thread_local Vector<KGraphNode> out;
	out.clear();
	out.emplace_back();
	size_t n = 0;
	Vector<const Form*> candidates;
	Vector<TypoCostInfo> candTypoCostStarts;
	auto* curNode = trie.root();
	auto* nextNode = trie.root();
	
	size_t lastSpecialEndPos = 0, specialStartPos = 0;
	POSTag chrType, lastChrType = POSTag::unknown, lastMatchedPattern = POSTag::unknown;
	auto branchOut = [&](size_t unkFormEndPos = 0, size_t unkFormEndPosWithSpace = 0, bool specialMatched = false)
	{
		if (!candidates.empty())
		{
			bool alreadySpecialChrProcessed = false;
			for (auto& cand : candidates)
			{
				const size_t nBegin = typoTolerant ? candTypoCostStarts[&cand - candidates.data()].start : (nonSpaces.size() - cand->sizeWithoutSpace());
				const auto scanStart = max(endPosMap[nBegin].first, (uint32_t)1), scanEnd = endPosMap[nBegin].second;
				const bool longestMatched = scanStart < scanEnd && any_of(out.begin() + scanStart, out.begin() + scanEnd, [&](const KGraphNode& g)
				{
					return nBegin == g.endPos && lastSpecialEndPos == g.endPos - (g.uform.empty() ? g.form->sizeWithoutSpace() : g.uform.size());
				});

				// insert unknown form 
				if (nBegin > lastSpecialEndPos && !longestMatched
					&& !isHangulCoda(cand->form[0]))
				{
					{
						size_t lastPos = out.back().endPos;

						if (lastPos < nBegin)
						{
							if (lastPos && isHangulCoda(str[nonSpaces[lastPos]])) lastPos--; // prevent coda to be matched alone.
							if (lastPos != lastSpecialEndPos)
							{
								appendNewNode(out, endPosMap, lastPos, str.substr(nonSpaces[lastPos], nonSpaces[nBegin] - nonSpaces[lastPos]), (uint16_t)nBegin);
							}
						}
					}

					const size_t newNodeLength = nBegin - lastSpecialEndPos;
					if (maxUnkFormSize && newNodeLength <= maxUnkFormSize)
					{
						appendNewNode(out, endPosMap, lastSpecialEndPos, str.substr(nonSpaces[lastSpecialEndPos], nonSpaces[nBegin] - nonSpaces[lastSpecialEndPos]), (uint16_t)nBegin);
					}
				}				

				// if special character
				if (cand->candidate[0] <= trie.value((size_t)POSTag::sn)->candidate[0])
				{
					// special character should be processed one by one chr.
					if (!alreadySpecialChrProcessed)
					{
						if (appendNewNode(out, endPosMap, nonSpaces.size() - 1, U16StringView{ cand->form.data() + cand->form.size() - 1, 1 }, (uint16_t)nonSpaces.size()))
						{
							out.back().form = trie.value((size_t)cand->candidate[0]->tag);
						}
						lastSpecialEndPos = nonSpaces.size();
						alreadySpecialChrProcessed = true;
					}
				}
				else
				{
					// TO DO: 아래의 spaceErrors 계산방식은 오타 교정 모드에서는 부정확한 값을 낼 수 있음. 더 정교한 방식으로 개선 필요
					const size_t lengthWithSpaces = countChrWithNormalizedSpace(nonSpaces.begin() + nBegin, nonSpaces.end());
					size_t spaceErrors = 0;
					if (lengthWithSpaces <= cand->form.size() + spaceTolerance 
						&& (!cand->numSpaces || (spaceErrors = countSpaceErrors(cand->form, nonSpaces.data() + nBegin, nonSpaces.data() + nonSpaces.size())) <= spaceTolerance))
					{
						if (!cand->numSpaces && lengthWithSpaces > cand->form.size()) spaceErrors = lengthWithSpaces - cand->form.size();
						const float typoCost = typoTolerant ? candTypoCostStarts[&cand - candidates.data()].cost : 0.f;
						if (appendNewNode(out, endPosMap, nBegin, cand, (uint16_t)nonSpaces.size(), typoCost))
						{
							out.back().spaceErrors = spaceErrors;
							if (typoTolerant)
							{
								out.back().typoFormId = candTypoCostStarts[&cand - candidates.data()].typoId;
							}
						}
					}
				}
			}
			candidates.clear();
			if (typoTolerant) candTypoCostStarts.clear();
		}
		else if (out.size() > 1 && !specialMatched)
		{
			size_t lastPos = out.back().endPos;
			if (lastPos < unkFormEndPos && !isHangulCoda(str[nonSpaces[lastPos]]))
			{
				appendNewNode(out, endPosMap, lastPos, str.substr(nonSpaces[lastPos], unkFormEndPosWithSpace - nonSpaces[lastPos]), (uint16_t)unkFormEndPos);
			}
		}

		const auto scanStart = max(endPosMap[unkFormEndPos].first, (uint32_t)1), scanEnd = endPosMap[unkFormEndPos].second;
		const bool duplicated = scanStart < scanEnd && any_of(out.begin() + scanStart, out.begin() + scanEnd, [&](const KGraphNode& g)
		{
			size_t startPos = g.endPos - (g.uform.empty() ? g.form->sizeWithoutSpace() : g.uform.size());
			return startPos == lastSpecialEndPos && g.endPos == unkFormEndPos;
		});
		if (unkFormEndPos > lastSpecialEndPos && !duplicated)
		{
			appendNewNode(out, endPosMap, lastSpecialEndPos, str.substr(nonSpaces[lastSpecialEndPos], unkFormEndPosWithSpace - nonSpaces[lastSpecialEndPos]), (uint16_t)unkFormEndPos);
		}
	};

	bool zCodaFollowable = false;
	const Form* const fallbackFormBegin = trie.value((size_t)POSTag::nng);
	const Form* const fallbackFormEnd = trie.value((size_t)POSTag::max);
	for (; n < str.size(); ++n)
	{
		char16_t c = str[n];
		char32_t c32 = c;
		if (isHighSurrogate(c32) && n + 1 < str.size())
		{
			c32 = mergeSurrogate(c32, str[n + 1]);
		}

		// Pretokenized 매칭
		if (pretokenizedFirst < pretokenizedLast && pretokenizedFirst->begin == n + startOffset)
		{
			if (lastChrType != POSTag::unknown)
			{
				// sequence of speical characters found
				if (lastChrType != POSTag::max && !isWebTag(lastChrType))
				{
					if (appendNewNode(out, endPosMap, specialStartPos, U16StringView{ &str[nonSpaces[specialStartPos]], n - nonSpaces[specialStartPos] }, (uint16_t)nonSpaces.size()))
					{
						out.back().form = trie.value((size_t)lastChrType);
					}
				}
				lastSpecialEndPos = specialStartPos;
				specialStartPos = nonSpaces.size();
			}

			uint32_t length = pretokenizedFirst->end - pretokenizedFirst->begin;
			branchOut(nonSpaces.size(), n);
			if (appendNewNode(out, endPosMap, nonSpaces.size(), pretokenizedFirst->form, nonSpaces.size() + length))
			{
				if (within(pretokenizedFirst->form, fallbackFormBegin, fallbackFormEnd))
				{
					out.back().uform = U16StringView{ &str[n], length };
				}
			}
			
			nonSpaces.resize(nonSpaces.size() + length);
			iota(nonSpaces.end() - length, nonSpaces.end(), n);
			n += length - 1;
			specialStartPos = lastSpecialEndPos = nonSpaces.size();
			pretokenizedFirst++;
			chrType = POSTag::max;
			curNode = trie.root();
			goto continueFor;
		}

		// 패턴 매칭
		{
			auto m = matchPattern(n ? str[n - 1] : u' ', str.data() + n, str.data() + str.size(), matchOptions);
			chrType = m.second;
			if (chrType != POSTag::unknown)
			{
				if (lastChrType != POSTag::unknown)
				{
					// sequence of speical characters found
					if (lastChrType != POSTag::max && !isWebTag(lastChrType))
					{
						if (appendNewNode(out, endPosMap, specialStartPos, U16StringView{ &str[nonSpaces[specialStartPos]], n - nonSpaces[specialStartPos] }, (uint16_t)nonSpaces.size()))
						{
							out.back().form = trie.value((size_t)lastChrType);
						}
					}
					lastSpecialEndPos = specialStartPos;
					specialStartPos = nonSpaces.size();
				}

				size_t patStart = nonSpaces.size();
				for (size_t i = 0; i < m.first; ++i)
				{
					branchOut(nonSpaces.size(), n + i, i > 0);
					nextNode = curNode->template nextOpt<arch>(trie, str[n + i]);
					while (!nextNode) // if curNode has no exact next node, goto fail
					{
						if (curNode->fail())
						{
							curNode = curNode->fail();
							for (auto submatcher = curNode; submatcher; submatcher = submatcher->fail())
							{
								const Form* cand = submatcher->val(trie);
								if (!cand) break;
								else if (!trie.hasSubmatch(cand))
								{
									if (!insertCandidates<typoTolerant>(candidates, candTypoCostStarts, cand, formBase, typoPtrs, str, nonSpaces)) break;
								}
							}
							nextNode = curNode->template nextOpt<arch>(trie, str[n + i]);
						}
						else
						{
							nonSpaces.emplace_back(n + i);
							goto continuePatternFor;
						}
					}
					nonSpaces.emplace_back(n + i);
					// from this, curNode has the exact next node
					curNode = nextNode;
					// if it has exit node, a pattern has found
					for (auto submatcher = curNode; submatcher; submatcher = submatcher->fail())
					{
						const Form* cand = submatcher->val(trie);
						if (!cand) break;
						else if (!trie.hasSubmatch(cand))
						{
							if (!insertCandidates<typoTolerant>(candidates, candTypoCostStarts, cand, formBase, typoPtrs, str, nonSpaces)) break;
						}
					}
				continuePatternFor:;
				}
				branchOut(nonSpaces.size(), n + m.first, true);

				if (appendNewNode(out, endPosMap, patStart, U16StringView{ &str[n], m.first }, (uint16_t)(patStart + m.first)))
				{
					out.back().form = trie.value((size_t)chrType);
				}

				n += m.first - 1;
				lastMatchedPattern = m.second;
				// SN태그 패턴 매칭의 경우 Web태그로 치환하여 Web와 동일하게 처리되도록 한다
				if (chrType == POSTag::sn)
				{
					chrType = POSTag::w_url;
					lastMatchedPattern = POSTag::w_url;
				}
				goto continueFor;
			}
		}

		chrType = identifySpecialChr(c32);

		if (lastChrType != chrType || lastChrType == POSTag::sso || lastChrType == POSTag::ssc)
		{
			// sequence of speical characters found
			if (lastChrType != POSTag::max && lastChrType != POSTag::unknown && lastChrType != lastMatchedPattern)
			{
				const auto scanStart = max(endPosMap[nonSpaces.size()].first, (uint32_t)1), scanEnd = endPosMap[nonSpaces.size()].second;
				const bool duplicated = scanStart < scanEnd && any_of(out.begin() + scanStart, out.begin() + scanEnd, [&](const KGraphNode& g)
				{
					return nonSpaces.size() == g.endPos;
				});
				if (nonSpaces.size() > lastSpecialEndPos && specialStartPos > lastSpecialEndPos && !duplicated)
				{
					appendNewNode(out, endPosMap, lastSpecialEndPos, str.substr(nonSpaces[lastSpecialEndPos], nonSpaces[specialStartPos] - nonSpaces[lastSpecialEndPos]), (uint16_t)specialStartPos);
				}

				if (lastChrType != POSTag::ss) // ss 태그는 morpheme 내에 등록된 후보에서 직접 탐색하도록 한다
				{
					if (appendNewNode(out, endPosMap, specialStartPos, U16StringView{ &str[nonSpaces[specialStartPos]], n - nonSpaces[specialStartPos] }, (uint16_t)nonSpaces.size()))
					{
						out.back().form = trie.value((size_t)lastChrType);
					}
				}
			}
			lastSpecialEndPos = (lastChrType == POSTag::sso || lastChrType == POSTag::ssc) ? nonSpaces.size() : specialStartPos;
			specialStartPos = nonSpaces.size();
		}
		lastMatchedPattern = POSTag::unknown;

		// 문장 종결 지점이 나타나거나 Graph가 너무 길어지면 공백 문자에서 중단
		if (chrType == POSTag::unknown && ((lastChrType == POSTag::sf && n >= 4) || n > 4096))
		{
			if (!isSpace(str[n - 3]) && !isSpace(str[n - 2]))
			{
				lastChrType = chrType;
				break;
			}
		}
		// 혹은 공백 문자가 아예 없는 경우 너무 길어지는 것을 방지하기 위해 강제로 중단
		else if (n >= 8192)
		{
			lastChrType = chrType;
			break;
		}

		// 공백문자를 무시하고 분할 진행
		if (chrType == POSTag::unknown)
		{
			branchOut(nonSpaces.size(), n);
			lastSpecialEndPos = nonSpaces.size();
			goto continueFor;
		}

		if (isOldHangulToneMark(c))
		{
			branchOut(nonSpaces.size(), n);
			goto continueFor;
		}

		nextNode = curNode->template nextOpt<arch>(trie, c);
		while (!nextNode) // if curNode has no exact next node, goto fail
		{
			if (curNode->fail())
			{
				curNode = curNode->fail();
				for (auto submatcher = curNode; submatcher; submatcher = submatcher->fail())
				{
					const Form* cand = submatcher->val(trie);
					if (!cand) break;
					else if (!trie.hasSubmatch(cand))
					{
						zCodaFollowable = zCodaFollowable || getZCodaAppendable<typoTolerant>(cand, formBase);
						if (!insertCandidates<typoTolerant>(candidates, candTypoCostStarts, cand, formBase, typoPtrs, str, nonSpaces)) break;
					}
				}
				nextNode = curNode->template nextOpt<arch>(trie, c);
			}
			else
			{
				if (chrType != POSTag::max)
				{
					branchOut(specialStartPos, specialStartPos < nonSpaces.size() ? nonSpaces[specialStartPos] : n);
				}
				else
				{
					branchOut();
				}
				
				// spaceTolerance == 0이고 공백 문자인 경우
				if (chrType == POSTag::unknown)
				{
					lastSpecialEndPos = nonSpaces.size();
				}
				// 그 외의 경우
				else
				{
					nonSpaces.emplace_back(n);
					if (c32 >= 0x10000) nonSpaces.emplace_back(++n);
					if (chrType != POSTag::max)
					{
						lastSpecialEndPos = nonSpaces.size();
					}
				}
				
				if (!!(matchOptions & Match::zCoda) && zCodaFollowable && isHangulCoda(c) && (n + 1 >= str.size() || !isHangulSyllable(str[n + 1])))
				{
					candidates.emplace_back(formBase + defaultTagSize + (c - 0x11A8) - 1);
					if (typoTolerant)
					{
						candTypoCostStarts.emplace_back(0, nonSpaces.size() - 1);
					}
				}
				zCodaFollowable = false;

				goto continueFor; 
			}
		}

		if (chrType != POSTag::max)
		{
			branchOut(specialStartPos, specialStartPos < nonSpaces.size() ? nonSpaces[specialStartPos] : n);
		}
		else
		{
			branchOut();
		}
		
		nonSpaces.emplace_back(n);

		if (!!(matchOptions & Match::zCoda) && zCodaFollowable && isHangulCoda(c) && (n + 1 >= str.size() || !isHangulSyllable(str[n + 1])))
		{
			candidates.emplace_back(formBase + defaultTagSize + (c - 0x11A8) - 1);
			if (typoTolerant)
			{
				candTypoCostStarts.emplace_back(0, nonSpaces.size() - 1);
			}
		}
		zCodaFollowable = false;

		// from this, curNode has the exact next node
		curNode = nextNode;
		// if it has exit node, patterns have been found
		for (auto submatcher = curNode; submatcher; submatcher = submatcher->fail())
		{
			const Form* cand = submatcher->val(trie);
			if (!cand) break;
			else if (!trie.hasSubmatch(cand))
			{
				zCodaFollowable = zCodaFollowable || getZCodaAppendable<typoTolerant>(cand, formBase);
				if (!insertCandidates<typoTolerant>(candidates, candTypoCostStarts, cand, formBase, typoPtrs, str, nonSpaces)) break;
			}
		}
	continueFor:
		lastChrType = chrType;
	}

	// sequence of speical characters found
	if (lastChrType != POSTag::max && lastChrType != POSTag::unknown && !isWebTag(lastChrType))
	{
		const auto scanStart = max(endPosMap[nonSpaces.size()].first, (uint32_t)1), scanEnd = endPosMap[nonSpaces.size()].second;
		const bool duplicated = scanStart < scanEnd && any_of(out.begin() + scanStart, out.begin() + scanEnd, [&](const KGraphNode& g)
		{
			return nonSpaces.size() == g.endPos;
		});
		if (nonSpaces.size() > lastSpecialEndPos && specialStartPos > lastSpecialEndPos  && !duplicated)
		{
			appendNewNode(out, endPosMap, lastSpecialEndPos, str.substr(nonSpaces[lastSpecialEndPos], nonSpaces[specialStartPos] - nonSpaces[lastSpecialEndPos]), (uint16_t)specialStartPos);
		}
		if (appendNewNode(out, endPosMap, specialStartPos, U16StringView{ &str[nonSpaces[specialStartPos]], n - nonSpaces[specialStartPos] }, (uint16_t)nonSpaces.size()))
		{
			out.back().form = trie.value((size_t)lastChrType);
		}
	}
	lastSpecialEndPos = specialStartPos;

	curNode = curNode->fail();
	while (curNode)
	{
		if (curNode->val(trie) && !trie.hasSubmatch(curNode->val(trie)))
		{
			const Form* cand = curNode->val(trie);
			if (!insertCandidates<typoTolerant>(candidates, candTypoCostStarts, cand, formBase, typoPtrs, str, nonSpaces)) break;
		}
		curNode = curNode->fail();
	}
	branchOut(nonSpaces.size(), n);

	appendNewNode(out, endPosMap, nonSpaces.size(), nullptr, nonSpaces.size() + 1);
	out.back().endPos = nonSpaces.size();

	nonSpaces.emplace_back(n);

	removeUnconnected(ret, out, endPosMap);
	for (size_t i = 1; i < ret.size() - 1; ++i)
	{
		auto& r = ret[i];
		r.startPos = nonSpaces[r.startPos] + startOffset;
		r.endPos = nonSpaces[r.endPos - 1] + 1 + startOffset;
	}
	ret.back().startPos = ret.back().endPos = str.size() + startOffset;
	while (n < str.size() && isSpace(str[n])) ++n;
	return n + startOffset;
}

template<ArchType arch>
const Form* kiwi::findForm(
	const utils::FrozenTrie<kchar_t, const Form*>& trie,
	const KString& str
)
{
	auto* node = trie.root();
	for (auto c : str)
	{
		node = node->template nextOpt<arch>(trie, c);
		if (!node) return nullptr;
	}
	if (trie.hasSubmatch(node->val(trie))) return nullptr;
	return node->val(trie);
}

namespace kiwi
{
	template<bool typoTolerant>
	struct SplitByTrieGetter
	{
		template<std::ptrdiff_t i>
		struct Wrapper
		{
			static constexpr FnSplitByTrie value = &splitByTrie<static_cast<ArchType>(i), typoTolerant>;
		};
	};
}

FnSplitByTrie kiwi::getSplitByTrieFn(ArchType arch, bool typoTolerant)
{
	static tp::Table<FnSplitByTrie, AvailableArch> table{ SplitByTrieGetter<false>{} };
	static tp::Table<FnSplitByTrie, AvailableArch> tableTT{ SplitByTrieGetter<true>{} };
	
	if (typoTolerant)
	{
		return tableTT[static_cast<std::ptrdiff_t>(arch)];
	}
	else
	{
		return table[static_cast<std::ptrdiff_t>(arch)];
	}
}

namespace kiwi
{
	struct FindFormGetter
	{
		template<std::ptrdiff_t i>
		struct Wrapper
		{
			static constexpr FnFindForm value = &findForm<static_cast<ArchType>(i)>;
		};
	};
}

FnFindForm kiwi::getFindFormFn(ArchType arch)
{
	static tp::Table<FnFindForm, AvailableArch> table{ FindFormGetter{} };

	return table[static_cast<std::ptrdiff_t>(arch)];
}
