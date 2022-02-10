class ExamException(Exception):
    pass


class CSVTimeSeriesFile(): 
    def __init__(self, name):
        self.name=name
        
    def get_data(self):

        if self.name != 'data.csv':
            raise ExamException('il file usato non è compattibile')

        try:
            file=open(self.name, 'r')
            file.readline()
        except:
            raise ExamException('Errore in apertura del file')
            
        time_series=[] #inizializzo una lista vuota  

        # Apro il file
        file = open(self.name, 'r')

        for line in file:
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

    if len(first_year) != 4 or len(last_year) != 4:
        raise ExamException('non è inserito un anno')


    first_year = int(first_year)
    last_year = int(last_year)

    if first_year < 1949:
        raise ExamException('il valore minimo non può essere minore di 1949')

    if last_year > 1960:
        raise ExamException('il valore massimo non può essere più di 1960')

    
    lista = []
    year = 0
    annoList = []
    for i in range(0,len(time_series)):
        data=time_series[i][0] #chiamo 'data' la stringa contenente anno e mese
        data=data.split('-') #divido la stringa 'data'
    
        anno=int(data[0]) #chiamo 'anno' la prima parte della stringa 'data'

        if anno >= first_year and anno <= last_year:
            
            if i == 0:
                year = anno

            if year == anno :
                meseList = []
                mese=int(data[1])
                meseList.append(mese) #aggiungo il mese alla lista new
                valore=int(time_series[i][1]) 
                meseList.append(valore) #aggiungo il numero dei passeggeri alla lista
                annoList.append(meseList)
            else:
                year = anno
                if len(annoList) > 0:
                    lista.append(annoList)
                annoList = []
                meseList = []
                mese=int(data[1])
                meseList.append(mese) #aggiungo il mese alla lista new
                valore=int(time_series[i][1]) 
                meseList.append(valore) #aggiungo il numero dei passeggeri alla lista
                annoList.append(meseList)

        else:
            if len(annoList) > 0:
                    lista.append(annoList)
                    annoList = []
                        
    for item in lista: 
        print(item) 
        #stampo gli elementi all'interno della lista 'lista'
        #ogni elemento della lista 'lista' è una lista, formata da tre valori interi, in cui il primo è l'anno, il secondo il mese e il terzo i passeggeri


    lista_variazioni=[] #lista da far tornare al metodo compute_avg_monthly_difference   

    for i in range(1,13):
        lista_valori=[]
        for y in range(0,len(lista)):

            if y > 0:

                m_pos= -1
                m_old_pos= -1
                for v in range(0,len(lista[y])):
                    if lista[y][v][0] == i:
                        m_pos = v

                for v in range(0,len(lista[y-1])):
                    if lista[y-1][v][0] == i:
                        m_old_pos = v

                if m_pos != -1 and m_old_pos != -1 :  

                    if lista[y][m_pos][0] == lista[y-1][m_old_pos][0]:
                        passenger_old = lista[y-1][m_old_pos][1]
                        passenger = lista[y][m_pos][1]
                        lista_valori.append(passenger-passenger_old)

                else: 
                    lista_valori.append(0)

        tot = 0
        if len(lista_valori) < 2:
            if  lista_valori == 0:
                lista_variazioni.append(tot)     
        else:
            for valore in lista_valori:
                tot = tot + valore
            if  lista_valori == 0:
                lista_variazioni.append(tot)
            else:
                lista_variazioni.append(tot/len(lista_valori))
        

    print('lista variazioni: {}'.format(lista_variazioni))
    return lista_variazioni


# corpo programma
time_series_file = CSVTimeSeriesFile(name='data.csv')

time_series = time_series_file.get_data()

avg_monthly_difference=compute_avg_monthly_difference(time_series, "1949", "1951") 


