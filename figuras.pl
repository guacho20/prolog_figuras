% Hechos que describen figuras geométricas
% figura(nombre, tiene_radio,numlados, tiene_angulo_recto).
figura(circulo, si,0,no).
figura(pentagono, no,5,no).
figura(triangulo, no,3,no).
figura(rectangulo, no,4, si).
figura(cuadrado, no,4, si).

% Regla principal para clasificar la figura geométrica
clasificar_figura(F, R, L, TAR) :-
    figura(F, R,L, TAR),!.

clasificar_figura(Figura, _, _, _) :-
    Figura = figura_desconocida,!.