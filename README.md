# mcts_backgammon

<h3>Node.py</h3>
<p>Clasa <b>Node</b> implementeaza toate cele 4 etape din algoritmul Monte Carlo Tree Search</p>
<ol>
  <li>
    select - Selecteaza cel mai promitator nod copil din lista comparand ratele de castig ale tuturor copiiilor
  </li>
  <li>
    expand - Promoveaza un nod frunza astfel: calculeaza miscarile posibile si le adauga ca si copiii nodului curent
  </li>
  <li>
    backprop - Propaga rezultatul unei simulari plecand de la nodurile frunza pana la radacina.
  </li>
  <li>
    simulate - Simuleaza un folosind miscari posibile dar aleatoare. 
  </li>
</ol>
<p>Alte metode ajutatoare ale clasei Node:</p>
<ul>
  <li>
    get_root - returneaza radacina arborelui de cautare
  </li>
  <li>
    compute_UCB - calculeaza scorul nodului , folosind numarul de vizite si numarul de castiguri impreuna cu o constanta
    formula folosita <i>self.wins/self.visits + c * math.sqrt(math.log(self.get_root().visits)/self.visits)</i>
  </li>
  <li>
    is_leaf_node - calculeaza daca nodul curent este nod frunza
  </li>
  <li>
    is_fully_expanded - calculeaza daca nodul curent a folosit toate miscarile posibile pentru a se extinde
  </li>
</ul>


<h3>Dice.py</h3>
  <p>Clasa <b>Dice</b> reprezinta zarurile folosite in joc. O pereche de zaruri este reprezentata intern printr-un vector care este folosit mai departe in functiile de generare a miscarilor posibile pentru ambii jucatrori.</p>

<h3>State.py</h3>
<p>
  Clasa <b>State</b> reprezinta starea in care se afla un joc de table. Intern tabla este reprezentata printr-un vector de lungime 25 care contine valori intregi. Culorile pieselor sunt reprezentate prin semnul intregului (- pentru negru si + pentru alb). 
  Clasa implementeaza urmatoarele metode:
  <ul>
    <li>__str__ - folosit pentru a afisa starea jocului in consola</li>
    <li>__eq__ - folosit pentru a compara 2 stari ale jocului (folosit in special pentru a gasi mutari unice . 2 mutari pot fi diferite dar pot rezulta o tabla identica )</li>
    <li>
      update_point_vectors - folosita pentru a actualiza cei 2 vectori care contin indicii coloanelor ocupate de catre alb sau negru , dupa efectuarea unei mutari
    </li>
    <li>
      copy- folosita pentru a copia starea (deep copy). Foarte utila atunci cand generam noduri noi in arborele de cautare Monte Carlo si le trimitem o pereche de stare si mutare.
    </li>
    <li>
      get_randomized_player_points - returneaza un vector amestecat aleator ce contine indicii coloanelor ocupate de un anumit jucator (alb/negru)
    </li>
    <li>
      get_player_points - returneaza un vector ce contine indicii coloanelor ocupate de un anumit jucator (alb/negru)
    </li>
    <li>
      get_points_taken - returneaza cate piese a pierdut un anumit jucator.
    </li>
    <li>
      can_take_off - calculeaza daca un anumit jucator are voie sa scoata piese de pe tabla
    </li>
    <li>
      game_is_finished - calculeaza daca jocul s-a terminat
    </li>
    <li>
      is_pip_state - calculeaza daca cei doi jucatori sunt "izolati"
    </li>
  </ul>
</p>
