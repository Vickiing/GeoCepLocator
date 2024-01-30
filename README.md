# GeoCepLocator
#Encontrar Latitude e Longitude por CEP
Este é um pequeno script Python que utiliza a biblioteca geopy para encontrar a latitude e longitude de um determinado CEP ou uma lista de CEPs e depois, exporta para um arquivo TXT.

Requisitos
Biblioteca geopy.

Uso:
Forneça um CEP na variável cep ou uma lista de ceps na variavél cep_list, como argumento para a função encontrar_lat_long_por_cep.
A função retornará a latitude e longitude correspondentes ao CEP fornecido.


Obs: Podem ocorrer erros de request, dependendo do numero de requisições e do período entre elas. Na maioria dos casos basta solicitar a execução do script novamente. 
