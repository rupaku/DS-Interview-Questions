'''
https://www.algoexpert.io/questions/Tournament%20Winner
'''
# Time O(n) | space O(k)
# n -> num of competitions
# k -> num of team in competition
HOME_TEAM_WON = 1
def tournamentWinner(competitions, results):
    # Write your code here.
    currentBestTeam=""
	scores={currentBestTeam:0}
	
	for idx, competition in enumerate(competitions):
		result= results[idx]
		hometeam,awayteam=competition
		
		winningteam= hometeam if result == HOME_TEAM_WON else awayteam
		updateScores(winningteam,3,scores)
		
		if scores[winningteam] > scores[currentBestTeam]:
			currentBestTeam = winningteam
	return currentBestTeam

def updateScores(team,points,scores):
	if team not in scores:
		scores[team] = 0
	scores[team] += points
	
	
'''
Test case
'''
import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
        results = [0, 0, 1]
        expected = "Python"
        actual = program.tournamentWinner(competitions, results)
        self.assertEqual(actual, expected)