import pandas as pd

class BAlbuns:
    def __init__(self):
        # Criação de dicionário com a lista de álbuns da banda Legião Urbana
         self.albuns = {'Nome': ['1-Legião Urbana',
                                '2-Dois',
                                '3-Que País é Este',
                                '4-As Quatro Estações',
                                '5-V',
                                '6-O Descobrimento do Brasil',
                                '7-A Tempestade',
                                '8-Uma Outra Estação'],
                       'Ano': [1985, 1986, 1987, 1989, 1991, 1993, 1996, 1997]}
    #metodo que mostra um dataframe com os albuns da legiao
    def mostrar_albuns(self):
        # Converter o dicionário em um DataFrame em Pandas
        print(f"=== Bem-vindo! Esta é uma lista dos álbuns da banda Legião Urbana ===")
        return pd.DataFrame(self.albuns)
    
if __name__ == '__main__' :
    ls_albuns = BAlbuns()
    print (ls_albuns.mostrar_albuns())
