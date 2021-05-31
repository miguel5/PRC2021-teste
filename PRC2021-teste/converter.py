import json

emds = json.load(open('C:\\Users\\Miguel\\Documents\\MIEI\\2021\\PRC\\PRC2021-teste\\emd.json'))

modalidades = []
clubes = []

with open('individuos.ttl', 'a', encoding='utf-8') as f:

    for emd in emds:

        nome = emd['nome']['primeiro'] + emd['nome']['ultimo']

        s = ''
        s = '###  http://www.semanticweb.org/miguel/ontologies/2021/emd#' + emd['_id'] + '\n'
        s = s + '       :' + emd['_id'] + ' rdf:type owl:NamedIndividual ,' + '\n'
        s = s + '       :EMD ;\n'
        s = s + '       :pertenceAoAtleta :' + nome + ' ;\n'
        s = s + '       :dataEMD :' + emd['dataEMD'] + ' ;\n'
        s = s + '       :index ' + '"' + str(emd['index']) + '"' + '^^xsd:string ;\n'
        s = s + '       :resultado ' + '"' + str(emd['resultado']) + '"' + '^^xsd:string .\n'

        f.write(s)

        s = ''
        s = s + '###  http://www.semanticweb.org/miguel/ontologies/2021/emd#' + nome + '\n'
        s = s + '       :' + nome + ' rdf:type owl:NamedIndividual ,\n' + '     :Atleta ;\n'
        s = s + '       :membroDo :' + emd['clube'] + ' ;\n'
        s = s + '       :praticaModalidade :' + emd['modalidade'] + ' ;\n'
        s = s + '       :temEMD :' + emd['_id'] + ' ;\n'
        s = s + '       :email ' + '"' + emd['email'] + '"' + '^^xsd:string ;\n'
        s = s + '       :federado ' + '"' + str(emd['federado']) + '"' + '^^xsd:string ;\n'
        s = s + '       :genero ' + '"' + emd['genero'] + '"' + '^^xsd:string ;\n'
        s = s + '       :idade ' + '"' + str(emd['idade']) + '"' + '^^xsd:string ;\n'
        s = s + '       :morada ' + '"' + emd['morada'] + '"' + '^^xsd:string ;\n'
        s = s + '       :pnome ' + '"' + emd['nome']['primeiro'] + '"' + '^^xsd:string ;\n'
        s = s + '       :unome ' + '"' + emd['nome']['ultimo'] + '"' + '^^xsd:string .\n'

        f.write(s)

        if emd['modalidade'] not in modalidades:
            s = ''
            s = '###  http://www.semanticweb.org/miguel/ontologies/2021/emd#' + emd['modalidade'] + '\n'
            s = s + '       :' + emd['modalidade'] + ' rdf:type owl:NamedIndividual ,' + '\n'
            s = s + '       :Modalidade ;\n'
            s = s + '       :éPraticadaPor :' + nome + ' .\n'

            f.write(s)

        if emd['clube'] not in clubes:
            s = ''
            s = '###  http://www.semanticweb.org/miguel/ontologies/2021/emd#' + emd['clube'] + '\n'
            s = s + '       :' + emd['modalidade'] + ' rdf:type owl:NamedIndividual ,' + '\n'
            s = s + '       :Clube ;\n'
            s = s + '       :temMembro :' + nome + ' .\n'

            f.write(s)

        

        
