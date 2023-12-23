class Puppy():
  def __init__(self, name, favourite_toy):
    self.name = name
    self.favourite_toy = favourite_toy

  def play(self):
    print(self.name + " is playing with the " + self.favourite_toy)

marble = Puppy('Marble','teddy bear')
marble.play()

marble = Puppy('Onyx', 'lizard')
marble.play()