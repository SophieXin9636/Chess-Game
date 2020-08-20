# Chess Game

## Case 1: Draw a chessboard

First chessboard is a initial board of standard position. <br>
Second chessboard is a board of random position. <br>

<img src="case1.png" width=40%> <br>

## Case 2: Move pieces from initial chessboard
* King 		`♚` (Input: K)
* Queen		`♛` (Input: Q)
* Rook		`♜` (Input: R)
* Bishop 	`♝` (Input: B)
* Knight 	`♞` (Input: N)
* Pawn   	`♟`

### Input Format
* **Movement:** Using `<piece1+position>`
	* Position should correct, and the piece movement should follow the piece's movement rule.
	* If piece2 is pawn, then do not input piece2, only position.
	* Position format: `<a-h><1-8>`
* **Capture:** Using `<piece1+position>x<piece2+position>`
	* Position should correct, and the piece movement should follow the piece's movement rule.
	* Cannot capture the same color pieces.
	* If piece2 is pawn, then do not input piece2, only position
	* e.g. If Black King capture White Pawn, then input is `K`e1xf7
	* e.g. If White Rook capture Knight, then input is Rh1xNh6 


### Movement
Input moving position, and the game would predict which pieces should move. <br>
First step is enter white piece movement, and then black. <br>
If the position is not correct (it means no piece can goto), then user should reinput again. <br>
<br>

<img src="case2_img.png"> <br>

<br>
Let's play the game! <br>
<br>
<img src="case2_step.png"> <br>

## Case 3: On input by case2

<img src="case3_1.png"> <br>

<img src="case3_2.png"> <br>

The last step would occur because using twice position movement intentionally. <br>

<img src="case3_3.png"> <br>