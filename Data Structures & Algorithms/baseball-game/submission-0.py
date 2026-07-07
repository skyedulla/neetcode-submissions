class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scoreboard = []
        for op in operations:
            if op == '+':
                score1 = scoreboard[-1]
                score2 = scoreboard[-2]
                scoreboard.append(score1 + score2)
            elif op == 'D':
                new_score = scoreboard[-1]
                scoreboard.append(new_score * 2)
            elif op == 'C':
                scoreboard.pop()
            else:
                scoreboard.append(int(op))

        return sum(scoreboard)