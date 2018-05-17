## 1. Minimax and Alphabeta

1.1 For the [first game tree on the HW3 page](mm0.png), use the minimax algorithm to compute a value for each non-leaf node. Squares represent max nodes and circles represent min nodes. Indicate which move the maximizing player should make.

See mm0_mm1_answers.pdf

1.2 Simulate the alpha-beta algorithm on the [second game tree on the HW3 page](mm1.png), crossing out the nodes that are pruned. For each non-leaf node that is not pruned, show the exact value (e.g., =3) or the last constraint (e.g., <= 2, >=8) that the alpha-beta algorithm determines.

See mm0_mm1_answers.pdf

## 2. Game characteristics

For each of the following statements, say whether it is true or false and provide a short (e.g. one paragraph) justification for your answer.

2.1 Given a two-player, turn-taking, zero-sum, fully observable game between two perfectly rational players, it does not help the first player's outcome to know what strategy the second player is using -- that is, what move the second player will make, given the first player's move.

True. The second player will play optimally, and so is perfectly predictable up to ties.  Knowing which of two equally good moves the opponent will make does not change the value of the game to the first player

2.2 Given a two-player, turn-taking, zero-sum, partially observable game between two perfectly rational players, it does not help the first player to know what move the second player will make, given the first player's move.

False. In a partially observable game, knowing the second player's move tells the first player additional information about the game state that would otherwise be available only to the second player. For example, in a card game, knowing the opponents next move may reveal one of the opponent's cards to the first player.

2.3 A perfectly rational backgammon-playing agent with unlimited resources never loses.

False.  Since backgammon involves an element of chance, a player may loose to being unlucky even if she plays perfectly

## 3. Answer the following questions for our the game of Nim.

3.1 For a Nim game with initial configuration [5,4,3], what is the shortest possible game in terms of plys?

The game will consist of three plys if player one takes the entire first row, then player two takes the entire second row, and player 1 takes the entire third row, ending The game.

3.2 For a Nim game with initial configuration [5,4,3], what is the longest possible game in terms of plys?

The game can involve twelve plys if each player always takes on stone from a pile when it is her turn.

3.3 For a Nim game with initial configuration [H1, H2, ... Hn] where the Hi values are all positive integers greater than 0 and n is greater than 0, what is the shortest possible game in terms of plys?

n

3.4 For a Nim game with initial configuration [H1, H2, ... Hn] where the Hi values are all positive integers greater than 0 and n is greater than 0, what is the longest possible game in terms of plys?

the sum of the Hi values


