import shell
import util
import wordsegUtil

############################################################
# Problem 1b: Solve the segmentation problem under a unigram model

class SegmentationProblem(util.SearchProblem):
    def __init__(self, query, unigramCost):
        self.query = query
        self.unigramCost = unigramCost

    def startState(self):
        pass
        # ### START CODE HERE ###
        return self.query
        # ### END CODE HERE ###

    def isEnd(self, state):
        pass
        # ### START CODE HERE ###
        return len(state)==0
        # ### END CODE HERE ###

    def succAndCost(self, state):
        pass
        # ### START CODE HERE ###
        rlt=[]
        if not self.isEnd(state):
            for i in range(len(state),0,-1):
                action=state[:i]
                cost=self.unigramCost(action)
                remainingText=state[len(action):]
                rlt.append((action,remainingText,cost))
        return rlt
        # ### END CODE HERE ###

def segmentWords(query, unigramCost):
    if len(query) == 0:
        return ''

    ucs = util.UniformCostSearch(verbose=0)
    ucs.solve(SegmentationProblem(query, unigramCost))

    # ### START CODE HERE ###
    wr=' '.join(ucs.actions)
    return wr
    # ### END CODE HERE ###

############################################################
# Problem 2b: Solve the vowel insertion problem under a bigram cost

class VowelInsertionProblem(util.SearchProblem):
    def __init__(self, queryWords, bigramCost, possibleFills):
        self.queryWords = queryWords
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def startState(self):
        pass
        # ### START CODE HERE ###
        return (self.queryWords[0],0)
        # ### END CODE HERE ###

    def isEnd(self, state):
        pass
        # ### START CODE HERE ###
        return state[1]==len(self.queryWords)-1
        # ### END CODE HERE ###

    def succAndCost(self, state):
        pass
        # ### START CODE HERE ###
        rlt = []
        index=state[1]+1
        # temp=self.queryWords[index]
        choices = self.possibleFills(self.queryWords[index]).copy()
        if len(choices)==0:
            choices.add(self.queryWords[index])
        for action in choices:
            cost=self.bigramCost(state[0],action)
            rlt.append((action, (action,index), cost))
        return rlt
        # ### END CODE HERE ###

def insertVowels(queryWords, bigramCost, possibleFills):
    pass
    # ### START CODE HERE ###
    if len(queryWords)==0:
        return ''
    else:
        queryWords.insert(0,wordsegUtil.SENTENCE_BEGIN)
    ucs=util.UniformCostSearch(verbose=1)
    ucs.solve(VowelInsertionProblem(queryWords,bigramCost,possibleFills))
    words = ' '.join(ucs.actions)
    return words
    # ### END CODE HERE ###

############################################################
# Problem 3b: Solve the joint segmentation-and-insertion problem

class JointSegmentationInsertionProblem(util.SearchProblem):
    def __init__(self, query, bigramCost, possibleFills):
        self.query = query
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def startState(self):
        pass
        # ### START CODE HERE ###
        return (self.query,wordsegUtil.SENTENCE_BEGIN)
        # ### END CODE HERE ###

    def isEnd(self, state):
        pass
        # ### START CODE HERE ###
        if len(state[0])==0:
            return True
        return False
        # ### END CODE HERE ###

    def succAndCost(self, state):
        pass
        # ### START CODE HERE ###
        rlt=[]
        for i in range(1,len(state[0])+1):
            sw=state[0][:i]
            remainWord=state[0][i:]
            choices=self.possibleFills(sw).copy()
            for item in choices:
                cost=self.bigramCost(state[1],item)
                rlt.append((item, (remainWord,item), cost))
        return rlt
        # ### END CODE HERE ###

def segmentAndInsert(query, bigramCost, possibleFills):
    if len(query) == 0:
        return ''

    # ### START CODE HERE ###
    ucsm = util.UniformCostSearch(verbose=1)
    ucsm.solve(JointSegmentationInsertionProblem(query,bigramCost,possibleFills))
    words=' '.join(ucsm.actions)
    return words
    # ### END CODE HERE ###

############################################################

if __name__ == '__main__':
    shell.main()
