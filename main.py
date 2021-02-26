from pymongo import MongoClient

#Inicializa BD
mongoClient = MongoClient('mongodb://localhost:27017/')
db = mongoClient.receitas_DB #Cria Database (se nao existir)
receitas = db.receitas #Cria Collection (se nao existir)
#A database so é criada após haver pelo menos um item adicionado dentro dela.

# ------------------------------------------------------------------------------------------------------------------------------------

# CREATE
receita = {
        "id": "232002",
        "name": "Torta de Amendoim",
        "calories": "11.856.519",
        "total_fat": "0.0",
        "sugar": "3,58E+02",
        "sodium": "0.0",
        "protein": "30.525.032",
        "saturated_fat": "0.0"
}
receitas.insert_one(receita) #insert_many() poderia ser chamado caso se quisesse criar vários itens ao mesmo tempo. Ex: receitas= [{},{},{}] insert_many(receitas)

# ------------------------------------------------------------------------------------------------------------------------------------

# READ
readLoc= receitas.find({'name': 'Torta de Amendoim'}) #Retorna a localização do objeto na memoria
read= receitas.find_one({'id': '232002'}) #Retorna o primeiro documento na collection
print(read)

# ------------------------------------------------------------------------------------------------------------------------------------

#UPDATE

receitas.update_one({'name': 'Torta de Amendoim'}, { "$set": { "name": "Torta de Limão" } }) 
print(receitas.find_one({'id': '232002'})) #Retorna o primeiro documento na collection
# ------------------------------------------------------------------------------------------------------------------------------------

# DELETE

receitas.delete_one({"name":"Torta de Limão"}) #Também pode ser utilizado delete_many() para atualizar multiplos itens
print(receitas.find_one({'id': '232002'})) #Retorna o primeiro documento na collection
print('fim')