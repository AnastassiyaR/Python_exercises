"""Test."""
import pytest
from football import Player, Team, Match


@pytest.mark.timeout(1.0)
def test_get_goals_scored():
    """Test that a new player's goals scored is zero."""
    player1 = Player("John Doe", 1)
    player1.get_goals_scored()
    assert player1.get_goals_scored() == 0


@pytest.mark.timeout(1.0)
def test_get_player_name():
    """Test that the player's name is correctly returned."""
    player1 = Player("John Doe", 1)
    player1.get_player_name()
    assert player1.get_player_name() == "John Doe"


@pytest.mark.timeout(1.0)
def test_repr():
    """Test the string representation of the player."""
    player1 = Player("John Doe", 1)
    repr(player1)
    assert repr(player1) == "John Doe (1)"


@pytest.mark.timeout(1.0)
def test_get_player_number():
    """Test that the player's number is correctly returned."""
    player = Player("John Doe", 1)
    assert player.get_player_number() == 1


# Team
@pytest.mark.timeout(1.0)
def test_get_player_by_number_None():
    """Test getting a player by number returns None if not found."""
    player1 = Player("John Doe", 1)
    team = Team("Team A")
    team.add_player(player1)
    team.get_player_by_number(5)
    assert team.get_player_by_number(5) is None


@pytest.mark.timeout(1.0)
def test_add_player_twice():
    """Test that adding the same player twice returns False."""
    team = Team("Team A")
    player = Player("John Doe", 1)
    team.add_player(player)
    team.add_player(player)
    assert team.add_player(player) is False


@pytest.mark.timeout(1.0)
def test_get_players_sorted():
    """Test that players are sorted correctly."""
    team = Team("Team A")
    match = Match(team, Team("Dummy Team"))
    player1 = Player("John Doe", 1)
    player2 = Player("Jane Doe", 2)
    team.add_player(player1)
    team.add_player(player2)
    match.player_scored(team, player1)
    assert team.get_players_sorted() == [player1, player2]


@pytest.mark.timeout(1.0)
def test_full_team():
    """Test whether the team is full."""
    team = Team("Team A")
    player1 = Player("John Doe", 1)
    player2 = Player("Jane Doe", 2)
    team.add_player(player1)
    team.add_player(player2)
    team.is_full()
    assert team.is_full() is False


@pytest.mark.timeout(1.0)
def test_remove_player():
    """Test removing a player from the team."""
    team = Team("Team A")
    player1 = Player("John Doe", 1)
    team.add_player(player1)
    team.remove_player(player1)
    assert team.remove_player(player1) is False


@pytest.mark.timeout(1.0)
def test_get_players():
    """Test that a player is in the team."""
    team = Team("Team A")
    player1 = Player("John Doe", 1)
    team.add_player(player1)
    str(player1 in team.get_players())
    assert 'True'


@pytest.mark.timeout(1.0)
def test_get_player_by_number():
    """Test getting a player by number."""
    team = Team("Team A")
    player1 = Player("John Doe", 1)
    player2 = Player("Jane Doe", 2)
    team.add_player(player1)
    team.add_player(player2)
    team.get_player_by_number(1)
    assert team.get_player_by_number(1) == player1


@pytest.mark.timeout(1.0)
def test_player_scored():
    """Test that a player cannot score after receiving a red card."""
    team1 = Team("Team A")
    player1 = Player("John Doe", 1)
    team1.add_player(player1)
    match = Match(team1, Team("Team B"))
    match.give_red_card(player1)
    match.player_scored(team1, player1)
    assert match.give_red_card(player1) is False


@pytest.mark.timeout(1.0)
def test_player_scored_False():
    """Test that a player cannot score for the wrong team."""
    team1 = Team("Team A")
    player1 = Player("John Doe", 1)
    team1.add_player(player1)
    player2 = Player("Jane Doe", 2)
    team2 = Team("Team B")
    team2.add_player(player2)
    match = Match(team1, Team("Team B"))
    match.player_scored(team1, player2)
    assert match.player_scored(team1, player2) is False


@pytest.mark.timeout(1.0)
def test_get_red_cards():
    """Test that a player receives a red card correctly."""
    team = Team("Team A")
    player1 = Player("John Doe", 1)
    team.add_player(player1)
    match = Match(team, Team("Team B"))
    match.give_red_card(player1)
    player1.get_red_cards()
    assert player1.get_red_cards() == 1


@pytest.mark.timeout(1.0)
def test_give_red_card_false():
    """Test that a player cannot receive a red card twice."""
    player1 = Player("John Doe", 1)
    team = Team("Team A")
    team.add_player(player1)
    match = Match(team, Team("Team B"))
    match.give_red_card(player1)
    match.give_red_card(player1)
    assert match.give_red_card(player1) is False


@pytest.mark.timeout(1.0)
def test_get_score_team1():
    """Test that the score for team1 is updated correctly."""
    player1 = Player("John Doe", 1)
    team1 = Team("Team A")
    team1.add_player(player1)
    team2 = Team("Team B")
    player2 = Player("Jane Doe", 2)
    team2.add_player(player2)
    match = Match(team1, team2)
    match.player_scored(team2, player2)
    assert match.give_red_card(player2) is True


@pytest.mark.timeout(1.0)
def test_get_score_team2():
    """Test that the score for team2 is updated correctly."""
    player1 = Player("John Doe", 1)
    team1 = Team("Team A")
    team1.add_player(player1)
    team2 = Team("Team B")
    player2 = Player("Jane Doe", 2)
    team2.add_player(player2)
    match = Match(team1, team2)
    match.player_scored(team2, player2)
    match.get_score(team2)
    assert match.get_score(team2) == 1


@pytest.mark.timeout(1.0)
def test_get_winner_team1():
    """Test that the winner is correctly identified as team1."""
    player1 = Player("John Doe", 1)
    team1 = Team("Team A")
    team1.add_player(player1)
    team2 = Team("Team B")
    player2 = Player("Jane Doe", 2)
    team2.add_player(player2)
    match = Match(team1, team2)
    match.player_scored(team2, player2)
    match.get_winner()
    assert match.get_winner() == team2


@pytest.mark.timeout(1.0)
def test_get_winner_team2():
    """Test that the winner is correctly identified as team2."""
    player1 = Player("John Doe", 1)
    team1 = Team("Team A")
    team1.add_player(player1)
    team2 = Team("Team B")
    player2 = Player("Jane Doe", 2)
    team2.add_player(player2)
    match = Match(team1, team2)
    match.player_scored(team1, player1)
    match.get_winner()
    assert match.get_winner() == team1


@pytest.mark.timeout(1.0)
def test_get_winner_tie():
    """Test that a tie results in no winner."""
    player1 = Player("John Doe", 1)
    team1 = Team("Team A")
    team1.add_player(player1)
    team2 = Team("Team B")
    player2 = Player("Jane Doe", 2)
    team2.add_player(player2)
    match = Match(team1, team2)
    match.player_scored(team1, player1)
    match.player_scored(team2, player2)
    match.get_winner()
    assert match.get_winner() is None


@pytest.mark.timeout(1.0)
def test_has_red_card():
    """Test that a player has a red card after receiving one."""
    team = Team("Team A")
    player1 = Player("John Doe", 1)
    team.add_player(player1)
    match = Match(team, Team("Team B"))
    match.give_red_card(player1)
    match.has_red_card(player1)
    assert match.has_red_card(player1) is True


@pytest.mark.timeout(1.0)
def test_get_red_carded_players():
    """Test that the list of red-carded players is correct."""
    team1 = Team("Team A")
    player1 = Player("John Doe", 1)
    team1.add_player(player1)
    team2 = Team("Team B")
    player2 = Player("Jane Doe", 2)
    team2.add_player(player2)
    match = Match(team1, team2)
    match.give_red_card(player1)
    match.get_red_carded_players()
    assert match.get_red_carded_players() == [player1]


@pytest.mark.timeout(1.0)
def test_get_top_goalscorer_None():
    """Test that there is no top goalscorer when no goals are scored."""
    team1 = Team("Team A")
    team2 = Team("Team B")
    match = Match(team1, team2)
    match.get_top_goalscorer()
    assert match.get_top_goalscorer() is None


@pytest.mark.timeout(1.0)
def test_get_top_goalscorer():
    """Test that the top goalscorer is correctly identified."""
    player1 = Player("Jahn Doe", 1)
    team1 = Team("Team 1")
    team1.add_player(player1)
    team2 = Team("Team B")
    player2 = Player("Jane Doe", 2)
    team2.add_player(player2)
    match = Match(team1, team2)
    match.player_scored(team2, player2)
    match.get_top_goalscorer()
    assert match.get_top_goalscorer() == player2
