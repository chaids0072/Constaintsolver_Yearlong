(define (problem bw-abcde)

(:domain blocksworld)

(:objects a b c d e)

(:init (on-table a) (clear a)

(on-table b) (clear b)

(on-table e) (clear e)

(on-table c) (on d c) (clear d)                                                                                             
(arm-free))

(:goal (and (on b d) (on c a) (on e c))))