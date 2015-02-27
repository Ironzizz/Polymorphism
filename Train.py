from Transportation import Transportation

class Train( Transportation ):

   def __init__( self, start, end, distance, noStation ):
      Transportation.__init__( self, start, end, distance)
      self.noStation = noStation

   def find_cost( self ):
      return 5 * self.noStation