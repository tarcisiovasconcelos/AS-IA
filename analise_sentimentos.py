import spacy
from googletrans import Translator

class AnaliseSentimentos: 

    """ 
        Classe para Realizar Análise de Sentimentos
        TODO: Caso necessário, instale o spacy e a biblioteca pt
        * Lexico original de: http://ontolp.inf.pucrs.br/Recursos/downloads-OpLexicon.php
    """ 
    def __init__(self):
        self.__nlp = spacy.load('pt_core_news_sm')
        self.__dicionario = {}
        self.__criaDicionario()
        self.__tradutor = Translator()

    """ Ler linha por linha do modelo lexico e adiciona no dicionario o valor e a polaridade """
    def __criaDicionario(self):
        #Busca o Lexico
        arquivo = open('./lexico.txt', 'r')
        linhas = arquivo.readlines()

        #Salva as palavras no dicionario
        for linha in linhas:
            dado = linha.split(',')
            self.__dicionario[dado[0]] = int(dado[2])
        #Encerra o arquivo
        arquivo.close()

    """ 
        Avalia se o texto é positivo ou negativo
        @param texto - String a ser avaliada
        @return {score: number | entidades: []}
    """
    def avalia(self, texto): 
        retorno = {'score': 0, 'entidades': []}

        texto = self.__tradutor.translate(texto, dest = "pt").text

        tokens = self.__nlp(texto)
        #Identifica as entidades
        retorno['entidades'] = tokens.ents
        
        #Avalia as polaridades das palavras
        for token in tokens:
            #Normaliza o texto
            palavra = str(token.lemma_).lower()

            #Checa se existe no dicionário
            if (palavra in self.__dicionario):
                retorno['score'] += self.__dicionario[palavra] 
                            
        return retorno