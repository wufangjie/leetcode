from collections import deque, Iterable

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_dict = {word: [0, set()] for word in wordList}
        if endWord not in word_dict:
            return []

        def bfs(word, flag):
            length = 1
            Q = deque((word, None))
            result = []
            while Q:
                word = Q.popleft()
                if word is None:
                    if result:
                        yield result
                    else:
                        yield len(Q)
                    if Q:
                        length += 1
                        Q.append(None)
                else:
                    for w in self.get_possible_word(word):
                        test, _ = word_dict.get(w, (float('nan'), None))
                        if test * flag < 0:
                            if flag < 0:
                                result.append((word, w))
                            else:
                                result.append((w, word))
                        elif test == 0:
                            word_dict[w][0] = flag * (length + 1)
                            Q.append(w)
                            word_dict[w][1].add(word)
                        elif abs(test) == length + 1:
                            word_dict[w][1].add(word)

        word_dict[beginWord] = -1, None
        word_dict[endWord] = 1, None
        gs = [bfs(beginWord, -1), bfs(endWord, 1)]
        lens = [0, 0]
        try:
            while True:
                i = 1 if lens[0] > lens[1] else 0
                test = next(gs[i])
                if isinstance(test, Iterable):
                    break
                else:
                    lens[i] = test
        except StopIteration:
            test = []

        results = []
        for pairs in test:
            temp = self._append([list(pairs)], word_dict, beginWord, 0)
            results.extend(self._append(temp, word_dict, endWord, -1))
        return results

    @staticmethod
    def get_possible_word(word, abc=[chr(i) for i in range(97, 123)]):
        for i, w in enumerate(word):
            for a in abc:
                if a != w:
                    yield word[:i] + a + word[i+1:]

    @staticmethod
    def _append(results, word_dict, stopWord, i):
        while True:
            results2 = []
            for case in results:
                if case[i] == stopWord:
                    return results
                for word in word_dict[case[i]][1]:
                    if i == 0:
                        results2.append([word] + case)
                    else:
                        results2.append(case + [word])
            results = results2



if __name__ == '__main__':
    Solution().findLadders('hit', 'cog', ["hot","dot","dog","lot","log", "cog"])
    Solution().findLadders('hit', 'zog', ["hot","dot","dog","lot","log", "cog"])
    Solution().findLadders('hot', 'dog', ["hot","dog"])
    import time
    tic = time.time()
    #Solution().ladderLength('sand', 'acne', dd)
    Solution().ladderLength('acne', 'sand', dd)
    print(time.time() - tic)

    beginWord = "magic"
    endWord = "pearl"
    wordList = ["flail","halon","lexus","joint","pears","slabs","lorie","lapse","wroth","yalow","swear","cavil","piety","yogis","dhaka","laxer","tatum","provo","truss","tends","deana","dried","hutch","basho","flyby","miler","fries","floes","lingo","wider","scary","marks","perry","igloo","melts","lanny","satan","foamy","perks","denim","plugs","cloak","cyril","women","issue","rocky","marry","trash","merry","topic","hicks","dicky","prado","casio","lapel","diane","serer","paige","parry","elope","balds","dated","copra","earth","marty","slake","balms","daryl","loves","civet","sweat","daley","touch","maria","dacca","muggy","chore","felix","ogled","acids","terse","cults","darla","snubs","boats","recta","cohan","purse","joist","grosz","sheri","steam","manic","luisa","gluts","spits","boxer","abner","cooke","scowl","kenya","hasps","roger","edwin","black","terns","folks","demur","dingo","party","brian","numbs","forgo","gunny","waled","bucks","titan","ruffs","pizza","ravel","poole","suits","stoic","segre","white","lemur","belts","scums","parks","gusts","ozark","umped","heard","lorna","emile","orbit","onset","cruet","amiss","fumed","gelds","italy","rakes","loxed","kilts","mania","tombs","gaped","merge","molar","smith","tangs","misty","wefts","yawns","smile","scuff","width","paris","coded","sodom","shits","benny","pudgy","mayer","peary","curve","tulsa","ramos","thick","dogie","gourd","strop","ahmad","clove","tract","calyx","maris","wants","lipid","pearl","maybe","banjo","south","blend","diana","lanai","waged","shari","magic","duchy","decca","wried","maine","nutty","turns","satyr","holds","finks","twits","peaks","teems","peace","melon","czars","robby","tabby","shove","minty","marta","dregs","lacks","casts","aruba","stall","nurse","jewry","knuth"]
