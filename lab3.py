import itertools
#9
class Comparator(object):
  def __init__(self, x):
    self.value = x
  def _cmp(self, value):
    return self.value - value

  def compare(self, other):
    try:
      return self._cmp(other.value)
    except AttributeError:
      return 1

# 10
class Dot(object):

  def __init__(self, *args):
    self.point = list(args)

  def __str__(self):
    return ','.join(map(str, self.point))

  def distance(self, other):
    if len(self.point) != len(other.point):
      raise ValueError
    return sum(map(lambda x, y: (x - y)**2, self.point, other.point))**0.5

  def middle(self, other):
    if len(self.point) != len(other.point):
      raise ValueError
    return Dot(*list(map(lambda x, y: (x + y) / 2.0, self.point, other.point)))


def guessSign(array):
  for i in itertools.permutations(array):
    s = ('+'.join(str(x) for x in i))
    positions = [pos for pos, char in enumerate(s) if char == '+']
    for j in positions:
      x = list(s)
      x[j]='=='
      s1=''.join(x)
      if (eval(s1)):
        return 'YES'
  return 'NO'



class Construct:

  automaton = []
  is_constructable = True

  def __init__(self):
    pass

  def _read(self):
    while True:
      d = input()
      if not d:
        break
      self.automaton.append(d)
    return

  def _set_vars(self):
    self.automaton = [a.split(' ') for a in self.automaton]
    self.automaton_details = {auto.pop(0): auto[1:] for auto in self.automaton[1:] if len(auto[1:]) > 0}
    self.atoms = [a for a in self.automaton if len(a) == 1]
    self.atoms = reduce(lambda x, y: x + y, self.atoms) if self.atoms else []

    return

  def _parse_automaton(self, details):
    if isinstance(details, list):
      for detail in details:
        self.parse_automaton(detail)

    elif isinstance(details, str) and (details in self.atoms):
      self.is_constructable = True

    elif isinstance(details, str) and (details in self.automaton_details):
      self.parse_automaton(automaton_details[details])

    else:
      self.is_constructable = False

    return

  def get_result(self):
    self._read()
    self._set_vars()
    self._parse_automaton(self.automaton[0][1:])

    return 'YES' if self.is_constructable else 'NO'

print(guessSign([123,234,345,12]))

c=Comparator(1)
print(c.compare(Comparator(4)))
