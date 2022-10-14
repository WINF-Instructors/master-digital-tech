# Ein Knoten ist ein einzelnes Element der 
# Linked List. Es zeigt auf seinen Nachfolger.
# Das ist ein Beispiel einer Klasse, also aus dem
# objektorientierten Paradigma.
class Node:
  # In Methoden fuer Python-Klassen ist der erste Parameter
  # immer der Verweis auf das eigene Objekt (wird oft als self)
  # bezeichnet. Objekte der Klasse Node kann man erzeugen z.B. 
  # durch Belegen der Variable a mit a = Node(1), was einen 
  # Knoten mit dem Wert 1 erzeugt, der keinen Nachfolger hat 
  # (die Zuweisungen im Konstruktor __init__, der beim
  # Erzeugen des Objekts aufgerufen wird sind mit Default-Parametern 
  # None zu Beginn belegt).
  # Die Methode __init__, die immer beim Erzeugen von Objekten aufgerufen
  # wird nennt man Konstruktor.
  # Der Konstruktor setzt zwei Attribute in der Klasse. Im Gegensatz zu 
  # anderen objektorientierten Sprachen muss man in Python die Attribute
  # nicht vorher deklarieren. Nach dem Erzeugen eines Objekts a vom Typ
  # Node kann man mittels a.data bzw. a.next auf die Attribute zugreifen.
  def __init__(self, data = None, next=None): 
    # Der Knoten beinhaltet Daten
    self.data = data
    # Hier ist der Zeiger auf den Nachfolger
    self.next = next

# Linked List hat lediglich eine Referenz 
# auf den ersten Knoten
class LinkedList:
  def __init__(self): 
    # None ist ein Nulltyp, der praktisch auf einen undefinierten Wert
    # hinweist. 
    self.head = None

# Mit der Methode wird hinten in die 
# Linked List ein neues Element, 
# ein neuer Knoten, eingefuegt
# Wieder ist hier self die Referenz auf das eigene Objekt.
# Hat man ein Objekt a vom Typ LinkedList, also das durch
# a = LinkedList() erzeugt wurde, dann kann man die Methode
# aufrufen durch a.insert(1) (im Beispiel fuege ich einen Knoten
# an, der den Wert 1 traegt).
# Man beachte, dass man den Funktionsaufruf nicht etwa mittels
# insert(a,1) verwendet, wie es eigentlich durch die Signatur der Funktion
# zu erwarten warte. Python setzt den self Parameter durch den
# Aufruf von a.insert(1) automatisch an die erste Stelle.
  def insert(self, data):
    newNode = Node(data)
    if self.head is not None:
      current = self.head
      while current.next is not None:
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  # Die Methode druckt die Linked List auf der
  # Standardausgabe aus. Sie ist iterativ
  # programmiert.
  def printLL_iterative(self):
    current = self.head
    while current is not None:
      print(current.data)
      current = current.next

  # Dieselbe Methode in einer rekursiven
  # Variante
  def printLL_recursive(self):
    # Die innere Funktion wird verwendet,
    # um damit einen Schritt zu machen.
    # Sie ruft sich selbst (rekursiv)
    # auf.
    def recursive_step(ll):
      if ll is not None:
        print(ll.data)
        recursive_step(ll.next)
    # Damit wird die rekursive Funktion
    # initial gestartet.
    recursive_step(self.head)

  # Die Methode konvertiert die Linked List
  # in eine Liste (einen Array).
  # Sie ist im prozeduralen Stil geschrieben.
  def ll_to_list_procedural(self):
    new_list = []
    current = self.head
    while current is not None:
      # Diese Zeile ist typisch fuer den prozeduralen
      # Stil: Wir manipulieren die Ergebnisliste, indem
      # wir das Element hinten zufuegen.
      new_list.append(current.data)
      current = current.next
    return new_list
  
  # Dieselbe Funktion zur Konvertierung der Linked List
  # in eine Standardliste im funktionalen Stil.
  def ll_to_list_functional(self):
    def recursive_step(ll, l):
      if ll is not None:
        # Im Gegensatz zum prozeduralen Stil wird
        # in jedem Rekursionsschritt eine neue
        # Liste erzeugt und als Parameter dem 
        # naechsten Aufruf uebergeben.
        return recursive_step(ll.next, l + [ll.data])
      else:
        return l
    return recursive_step(self.head, [])

  # Dies ist ein Beispiel einer higher-order function.
  # Sie erhaelt eine Funktion als Parameter.
  # Die Idee, die Funktion ueberhaupt einzufuehren ist, 
  # dass man oben in ll_to_list_functional und printLL_recursive
  # im Grunde immer dieselben Muster sieht:
  # Im ersten Schritt wird geprueft ob man im letzten
  # Knoten angekommen ist (check ob None) und danach wird
  # eine Funktion ausgefuehrt, die etwas in irgendeiner Form
  # sammelt. Danach geht man rekursiv durch die ganze Liste.
  # Anstatt nun fuer jeden Use Case (Liste aus Linked List erzeugen,
  # Liste ausdrucken) eine eigene Funktion zu schreiben, die im 
  # Grunde immer demselben Prinzip folgt, schreibt man 
  # lieber eine higher-order function, die den gemeinsamen Teil
  # der Use Cases abdeckt und dann Funktionen, die jeweils diese
  # Funktion verwenden. Ein super Beispiel fuer Abstraktion,
  # die Anwendung des DRY Prinzips (Vermeiden von Redundanzen)
  # und der typischen Denkweise im funktionalen Umfeld.
  # f ist hier eine Funktion, die zwei Argumente hat und einen Wert zurueckgibt.
  # Das erste Argument ist eines, das die Resultate aufnimmt (unten collect genannt),
  # das zweite ist fuer einen Wert aus der Liste gedacht. 
  # Der Parameter init ist der Initialwert fuer collect.
  # Python ist nicht streng typisiert. Man kann hier so behelfsmaessige
  # Typen annotieren, aber die werden ohnehin nicht geprueft.
  # In streng typisierten Sprachen wie Java, C++ oder Scala muss man immer
  # Typen mitgeben. Damit kann man schon zur Compile-Time viele Fehler
  # ausschliessen, was besonders wichtig ist, wenn man so komplizierte
  # Strukturen wie inner functions oder higher-order Functions hat
  def reduce(self, f, init):
    def recursive_step(node, collect):
      if node is not None:
        return recursive_step(node.next, f(collect,node.data))
      else:
        return collect
    return recursive_step(self.head, init)
  
  # Hier wird nun die Konvertierung zur Standardliste durch Anwenden der neuen
  # reduce-Funktion durchgefuehrt. Es ist schon cool wie wir den ganzen Code
  # der Funktion ll_to_list_functional in eine Zeile gebracht haben. 
  # Ok, wir haben auch reduce geschrieben. Aber in der print-Funktion unten
  # sieht man super, wie man reduce wiederverwenden kann.
  def ll_to_list_via_reduce(self):
    # lambda spezifiziert eine Funktion (das ist unser f fuer reduce), die 
    # anonym ist, also keinen Namen erhaelt (weil wir sie ansonsten nicht wieder
    # verwenden). x ist hier faktisch das "collect" und y der Wert in der Liste,
    # bei dem wir aktuell sind wenn reduce ausgefuehrt wird. Die Funktion packt 
    # diesen Wert y hinten an die Liste dran (+ erzeugt eine neue Liste, also
    # keine Seiteneffekte wie es das funktionale Paradigma haben will). [], die
    # leere Liste ist der Initialwert.
    return self.reduce(lambda x,y: x+[y], [])

  # Hier nun die reduce-Variante fuer print. Da wir rein funktional unterwegs sein
  # wollen, druckt die Funktion nicht direkt aus sondern gibt einen String zurueck.
  # Den kann man dann hinterher ausdrucken. Funktional bedeutet insbesondere
  # dass man wie in der Mathematik Eingabewerte auf Ausgabewerte abbildet - ohne
  # Seiteneffekte. Wenn man funktional programmiert, aber Seiteneffekte haben will, 
  # dann schiebt man die Seiteneffekte soweit wie moeglich nach aussen bzw.
  # man trennt den funktionalen Teil von dem Teil mit Seiteneffekten.
  # Warum ist das wichtig? Weil man u.A. funktionale Teile ohne Seiteneffekte
  # super parallel verarbeiten kann (s. Vorlesung).
  def print_ll_via_reduce(self):
    # Hier ist unser collect ein String und ich packe das aktuelle Element, das
    # reduce rekursiv besucht hinten an den String, jeweils getrennt vom vorigen
    # durch einen line feed (Zeilenumbruch), der mit \n codiert wird.
    return self.reduce(lambda x,y: x+"\n"+str(y), "")
   
# Diese Bedingung ist so ein Python best practice. Koennt ihr ignorieren.
# Danach kommt nach all der Vorbereitung auf jeden Fall der Code, der
# nun mittels der oben definierten Klassen und Methoden ausgefuehrt wird.
if __name__ == '__main__':
  LL = LinkedList()
  LL.insert(3)
  LL.insert(4)
  LL.insert(5)
  LL.printLL_iterative()
  LL.printLL_recursive()
  l = LL.ll_to_list_procedural()
  print(l)
  l2 = LL.ll_to_list_functional()
  print(l2)
  l3 = LL.ll_to_list_via_reduce()
  print(l3)
  print(LL.print_ll_via_reduce())