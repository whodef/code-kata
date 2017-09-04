;;
;; Brute force Sudoku solver
;;
;; In Sudoku, the board is a 9x9 grid of SQUARES.
;; There are 9 ROWS and 9 COLUMNS, there are also 9
;; 3x3 BOXES.  Rows, columns and boxes are all UNITs.
;; So there are 27 units.
;;
;; The idea of the game is to fill each square with
;; a Natural[1, 9] such that no unit contains a duplicate
;; number.
;;


;; Data definitions:


;; Val is Natural[1, 9]

;; Board is (listof Val|false)   that is 81 elements long
;; interp.
;;  Visually a board is a 9x9 array of squares, where each square
;;  has a row and column number (r, c).  But we represent it as a
;;  single flat list, in which the rows are layed out one after
;;  another in a linear fashion. (See interp. of Pos below for how
;;  we convert back and forth between (r, c) and position in a board.)

;; Pos is Natural[0, 80]
;; interp.
;;  the position of a square on the board, for a given p, then
;;    - the row    is (quotient p 9)
;;    - the column is (remainder p 9)

(define (r-c->pos r c) (+ (* r 9) c))  ;helpful for writing tests


;; Unit is (listof Pos) of length 9
;; interp. 
;;  The position of every square in a unit. There are
;;  27 of these for the 9 rows, 9 columns and 9 boxes.


;; Constants:

(define ALL-VALS (list 1 2 3 4 5 6 7 8 9))

(define B false) ;B stands for blank


(define BD1 
  (list B B B B B B B B B
        B B B B B B B B B
        B B B B B B B B B
        B B B B B B B B B
        B B B B B B B B B
        B B B B B B B B B
        B B B B B B B B B
        B B B B B B B B B
        B B B B B B B B B))

(define BD2 
  (list 1 2 3 4 5 6 7 8 9 
        B B B B B B B B B 
        B B B B B B B B B 
        B B B B B B B B B 
        B B B B B B B B B
        B B B B B B B B B
        B B B B B B B B B
        B B B B B B B B B
        B B B B B B B B B))

(define BD3 
  (list 1 B B B B B B B B
        2 B B B B B B B B
        3 B B B B B B B B
        4 B B B B B B B B
        5 B B B B B B B B
        6 B B B B B B B B
        7 B B B B B B B B
        8 B B B B B B B B
        9 B B B B B B B B))

(define BD4                ;easy
  (list 2 7 4 B 9 1 B B 5
        1 B B 5 B B B 9 B
        6 B B B B 3 2 8 B
        B B 1 9 B B B B 8
        B B 5 1 B B 6 B B
        7 B B B 8 B B B 3
        4 B 2 B B B B B 9
        B B B B B B B 7 B
        8 B B 3 4 9 B B B))

(define BD4s               ;solution to 4
  (list 2 7 4 8 9 1 3 6 5
        1 3 8 5 2 6 4 9 7
        6 5 9 4 7 3 2 8 1
        3 2 1 9 6 4 7 5 8
        9 8 5 1 3 7 6 4 2
        7 4 6 2 8 5 9 1 3
        4 6 2 7 5 8 1 3 9
        5 9 3 6 1 2 8 7 4
        8 1 7 3 4 9 5 2 6))

(define BD5                ;hard
  (list 5 B B B B 4 B 7 B
        B 1 B B 5 B 6 B B
        B B 4 9 B B B B B
        B 9 B B B 7 5 B B
        1 8 B 2 B B B B B 
        B B B B B 6 B B B 
        B B 3 B B B B B 8
        B 6 B B 8 B B B 9
        B B 8 B 7 B B 3 1))

(define BD5s               ;solution to 5
  (list 5 3 9 1 6 4 8 7 2
        8 1 2 7 5 3 6 9 4
        6 7 4 9 2 8 3 1 5
        2 9 6 4 1 7 5 8 3
        1 8 7 2 3 5 9 4 6
        3 4 5 8 9 6 1 2 7
        9 2 3 5 4 1 7 6 8
        7 6 1 3 8 2 4 5 9
        4 5 8 6 7 9 2 3 1))

(define BD6                ;hardest ever? (Dr Arto Inkala)
  (list B B 5 3 B B B B B 
        8 B B B B B B 2 B
        B 7 B B 1 B 5 B B 
        4 B B B B 5 3 B B
        B 1 B B 7 B B B 6
        B B 3 2 B B B 8 B
        B 6 B 5 B B B B 9
        B B 4 B B B B 3 B
        B B B B B 9 7 B B))

(define BD7                 ; no solution 
  (list 1 2 3 4 5 6 7 8 B 
        B B B B B B B B 2 
        B B B B B B B B 3 
        B B B B B B B B 4 
        B B B B B B B B 5
        B B B B B B B B 6
        B B B B B B B B 7
        B B B B B B B B 8
        B B B B B B B B 9))




;; Positions of all the rows, columns and boxes:

(define ROWS
  (list (list  0  1  2  3  4  5  6  7  8)
        (list  9 10 11 12 13 14 15 16 17)
        (list 18 19 20 21 22 23 24 25 26)
        (list 27 28 29 30 31 32 33 34 35)
        (list 36 37 38 39 40 41 42 43 44)
        (list 45 46 47 48 49 50 51 52 53)
        (list 54 55 56 57 58 59 60 61 62)
        (list 63 64 65 66 67 68 69 70 71)
        (list 72 73 74 75 76 77 78 79 80)))

(define COLS
  (list (list 0  9 18 27 36 45 54 63 72)
        (list 1 10 19 28 37 46 55 64 73)
        (list 2 11 20 29 38 47 56 65 74)
        (list 3 12 21 30 39 48 57 66 75)
        (list 4 13 22 31 40 49 58 67 76)
        (list 5 14 23 32 41 50 59 68 77)
        (list 6 15 24 33 42 51 60 69 78)
        (list 7 16 25 34 43 52 61 70 79)
        (list 8 17 26 35 44 53 62 71 80)))

(define BOXES
  (list (list  0  1  2  9 10 11 18 19 20)
        (list  3  4  5 12 13 14 21 22 23)
        (list  6  7  8 15 16 17 24 25 26)
        (list 27 28 29 36 37 38 45 46 47)
        (list 30 31 32 39 40 41 48 49 50)
        (list 33 34 35 42 43 44 51 52 53)
        (list 54 55 56 63 64 65 72 73 74)
        (list 57 58 59 66 67 68 75 76 77)
        (list 60 61 62 69 70 71 78 79 80)))

(define UNITS (append ROWS COLS BOXES))




;; Functions:


;; Board -> Board or false
;; produce solution for bd; or false if bd is unsolvable
;; Assumption: bd is valid
(check-expect (solve BD4) BD4s)
(check-expect (solve BD5) BD5s)
(check-expect (solve BD7) false)

; 
; Backtracking search through arbitrary-arity search tree.
; 
; Generative recursion.
; 
; Termination argument:
;  trivial case:  checked board has no blanks
;  reduction step: fill first blank with all possible valid values
;  argument: the reduction step fills the blanks board by one, so
;            eventually the board will be full. 
;            
;            


(define (solve bd)
  (local [(define (solve/one bd)
            (if (solved? bd)
                bd 
                (solve/list (next-boards bd))))
          
          (define (solve/list lobd)
            (cond [(empty? lobd) false]
                  [else
                   (local [(define try (solve/one (first lobd)))]
                     (if (not (false? try))
                         try
                         (solve/list (rest lobd))))]))
          
          (define (next-boards bd)
            (local [(define blank (find-blank bd))] ;position of blank
              (filter valid-board?                  ;valid next boards
                      (map (λ (v) (bsubst bd blank v))
                           ALL-VALS))))]
    
    (solve/one bd)))

; ASIDE: For the really curious, lookup what the function curry does, and then
; replace the definition of solve/one above with the following. You'll need to
; put (require racket/function) at the top of the file for it to work. Its kind
; of neat.
; 
;           (define (solve/one bd)
;             (if (solved? bd)
;                 bd                   
;                 (solve/list 
;                  (filter check-board?
;                          (map (curry bsubst bd (find-blank bd)) ALL-VALS)))))
; 


;; Board -> Boolean
;; produce true if board has no blank squares
(check-expect (solved? BD1) false)
(check-expect (solved? (list 1 1)) true) ;white box test

(define (solved? bd) (andmap number? bd))


;; Board -> Pos
;; Produce the position of a blank square in bd
;; ASSUMPTION: the board contains at least 1 blank square
(check-expect (find-blank BD1) (r-c->pos 0 0))
(check-expect (find-blank BD2) (r-c->pos 1 0))
(check-expect (find-blank BD3) (r-c->pos 0 1))
(check-expect (find-blank BD4) (r-c->pos 0 3))
(check-expect (find-blank BD5) (r-c->pos 0 1))

(define (find-blank lovf)
  (cond [(empty? lovf) (error "Board should have contained at least one blank.")]
        [else
         (if (false? (first lovf))
             0
             (add1 (find-blank (rest lovf))))]))


;; Board -> Boolean
;; produce true if no unit on bd contains duplicate values; false otherwise
(check-expect (valid-board? BD1) true)
(check-expect (valid-board? BD2) true)
(check-expect (valid-board? BD3) true)
(check-expect (valid-board? BD4) true)
(check-expect (valid-board? BD5) true)
(check-expect (valid-board? (cons 2 (rest BD2))) false)
(check-expect (valid-board? (cons 2 (rest BD3))) false)
(check-expect (valid-board? (append (list 2 6) (rest (rest BD4)))) false)

(define (valid-board? bd)
  (local [(define (check-units lou)
            (andmap check-unit lou))     
          (define (check-unit u)
            (no-duplicates? (map (λ (p) (bref bd p)) u)))
          (define (no-duplicates? vals)
            (cond [(empty? vals) true]
                  [else
                   (if (and (number? (first vals))
                            (member (first vals) (rest vals)))
                       false
                       (no-duplicates? (rest vals)))]))]
    (check-units UNITS)))


;; Board Pos -> Val or false
;; Produce value at given position on board.
(check-expect (bref BD2 (r-c->pos 0 5)) 6)
(check-expect (bref BD3 (r-c->pos 7 0)) 8)

; 
; Function on 2 complex data: Board and Position (Position is Natural[0, 80]).
; We can assume that p is <= (length bd).
; 
;               empty     (cons Val-or-False Board)
;  0             XXX         (first bd)
;  
;  (add1 p)      XXX         <natural recursion>


(define (bref bd p)
  #;
  (cond [(zero? p) (first bd)]
        [else
         (bref (rest bd) (sub1 p))])

  (list-ref bd p))                    ;Dr Racket's version is faster!


;; Board Pos Val -> Board
;; produce new board with val at given position
(check-expect (bsubst BD1 (r-c->pos 0 0) 1)
              (cons 1 (rest BD1)))

; 
; Function on 2 complex data, Board and Position (which is Natural[0, 80]).
; We can assume that p is <= (length bd).
; 
;               empty     (cons Val-or-False Board)
;  0             XXX         (cons nv (rest bd))
;  
;  (add1 p)      XXX         (cons (first bd) <natural recursion>)


(define (bsubst bd p nv)
  (cond [(zero? p) (cons nv (rest bd))]
        [else
         (cons (first bd)
               (bsubst (rest bd) (sub1 p) nv))]))

