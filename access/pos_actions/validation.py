

class CL_posvalid(object):

    def FN_GtinValid(self,gtin):
        if len(gtin)>13 or len(gtin)<8:
            return False
        else:
            return True

