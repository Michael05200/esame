class ExamException(Exception):
    pass


class CSVTimeSeriesFile(): 
    def __init__(self, name):
        self.name=name
        
    def get_data(self):    

      

        try:
            my_file=open(self.name, 'r')
            my_file.readline()
        except:
            raise ExamException('Errore in apertura del file')
            
        time_series=[] #inizializzo una lista vuota  

        # Apro il file
        my_file = open(self.name, 'r')

        for line in my_file:
            #leggo il file riga per riga
            elements=line.split(',')
            elements[1] = elements[1].strip()

            if elements[0] != 'date':
            #se non sto processando l'intestazione, associo gli elementi      
              time_series.append(elements)
                #aggiungo gli elementi sottoforma di lista nella lista inizializzata precedentemente

        for item in time_series:
            print(item) #stampo gli elementi della lista

        return time_series


def compute_avg_monthly_difference(time_series, first_year, last_year):
    #serie storica=time_series
    #primo anno=data anno
    #ultimo anno=data anno

    lista=[]

    first_year = int(first_year)
    last_year = int(last_year)

    for serie in time_series:

        new=[] #creo una lista vuota in cui aggiungerò per ogni riga: anno, mese e passeggeri
        data=serie[0] #chiamo 'data' la stringa contenente anno e mese
        data=data.split('-') #divido la stringa 'data'
    
        anno=int(data[0]) #chiamo 'anno' la prima parte della stringa 'data'
        
        if anno >= first_year and anno <= last_year:

            #passo da stringa a valore intero
            new.append(anno) #aggiungo l'anno alla lista 

            mese=int(data[1])
            #chiamo la seconda parte della stringa riguardante la data 'mese' e la passo come valore intero
            new.append(mese) #aggiungo il mese alla lista new
            valore=int(serie[1]) 
            new.append(valore) #aggiungo il numero dei passeggeri alla lista
            
            lista.append(new) 
    
    for item in lista: 
        print(item) 
        #stampo gli elementi all'interno della lista 'lista'
        #ogni elemento della lista 'lista' è una lista, formata da tre valori interi, in cui il primo è l'anno, il secondo il mese e il terzo i passeggeri

    lista_variazioni=[] #lista da far tornare al metodo compute_avg_monthly_difference
    
    for i in range(1,13):
        lista_valori=[]
        for y in range(0,len(lista)):
            if lista[y][0] != first_year:
                if lista[y][1] == i:
                    passenger_old = lista[y-12][2]
                    passenger = lista[y][2]
                    lista_valori.append(passenger-passenger_old)
        tot = 0
        for valore in lista_valori:
            tot = tot + valore
        lista_variazioni.append(tot/len(lista_valori))     
    print('lista variazioni: {}'.format(lista_variazioni))
    return lista_variazioni


# corpo programma
time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
avg_monthly_difference=compute_avg_monthly_difference(time_series, "1949", "1960") 