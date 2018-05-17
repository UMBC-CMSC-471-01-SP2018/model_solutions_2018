;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; HW5 blocks world 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (domain hw5_domain)
  (:requirements :strips)

  (:constants red green blue)

  (:predicates (on ?x ?y)
	       (on-table ?x)
	       (clear ?x)
	       (arm-empty)
	       (holding ?x)
	       (color ?x ?color)
	       (block ?x)
	       (paint-can ?x ?color)
               (open ?can)
	       (brush ?x)
	       (water-bucket ?wb)
	       (clean ?brush)
	       (loaded ?brush ?color) )

  (:action pick-up
	     :parameters (?ob1)
	     :precondition (and (clear ?ob1) (on-table ?ob1) (arm-empty))
	     :effect
	     (and (not (on-table ?ob1))
		   (not (clear ?ob1))
		   (not (arm-empty))
		   (holding ?ob1)))

  (:action put-down
	     :parameters (?ob)
	     :precondition (holding ?ob)
	     :effect
	     (and (not (holding ?ob))
		   (clear ?ob)
		   (arm-empty)
		   (on-table ?ob)))

  (:action stack
	     :parameters (?sob ?sunderob)
	     :precondition (and (holding ?sob) (clear ?sunderob))
	     :effect
	     (and (not (holding ?sob))
		   (not (clear ?sunderob))
		   (clear ?sob)
		   (arm-empty)
		   (on ?sob ?sunderob)))

  (:action unstack
	     :parameters (?sob ?sunderob)
	     :precondition (and (on ?sob ?sunderob) (clear ?sob) (arm-empty))
	     :effect
	     (and (holding ?sob)
		   (clear ?sunderob)
		   (not (clear ?sob))
		   (not (arm-empty))
		   (not (on ?sob ?sunderob))))

  (:action paint
	     :parameters (?obj ?color ?brush)
	     :precondition (and (on-table ?obj)
	     		   	(clear ?obj)
	     		   	(brush ?brush)
			   	(holding ?brush)
				(loaded ?brush ?color) )
	     :effect (color ?obj ?color))

  (:action wash-brush
     :parameters (?brush ?wb ?color)
     :precondition (and (brush ?brush)
     		   	(holding ?brush)
     		        (loaded ?brush ?color)
			(water-bucket ?wb)
			(clear ?wb))
     :effect (and (not (loaded ?brush ?color))
     	     	  (clean ?brush)))

  (:action load-brush
     :parameters (?brush ?can ?color)
     :precondition (and (brush ?brush)
     		   	(clean ?brush)
			(holding ?brush)
			(paint-can ?can ?color)
			(clear ?can)
                        (open ?can))
     :effect (and (loaded ?brush ?color)
     	          (not (clean ?brush))))

   (:action remove-can-lid 
     :parameters (?can ?color)
     :precondition (and (paint-can ?can ?color)
                         (not (open ?can))
   		         (clear ?can)
                         (arm-empty))
     :effect (open ?can))


   (:action replace-can-lid
     :parameters (?can ?color)
     :precondition (and (paint-can ?can ?color)
                         (open ?can)
   			 (clear ?can)
                         (arm-empty))
     :effect (not (open ?can)))

)
