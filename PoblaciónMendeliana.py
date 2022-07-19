# Generación de Población
import scipy
def build_population(N, p):
    """
    Se crea una población en la cual N es el número de individuos. Además cada individuo tiene 2 cromosomas
    que contienen un alelo "A" o un alelo "a", con una probabilidad p de 1-p. La población se expresará en 
    una lista de tuplas.
    """
    population = []
    for i in range(N):
        allele1 = "A"
        if scipy.random.rand() > p:
            allele1 = "a"
        allele2 = "A"
        if scipy.random.rand() > p:
            allele2 = "a"
        population.append((allele1, allele2))
    return population

# Conteo de frecuencia de alelos
def compute_frequencies(population):
    """ 
    Aquí se hace un conteo del genotipo. También se detecta la proporción de cada alelo requerido en proporción a los demás alelos. 
    """
    AA = population.count(("A", "A"))
    Aa = population.count(("A", "a"))
    aA = population.count(("a", "A"))
    aa = population.count(("a", "a"))
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA})

# Reproducción de la población 
def reproduce_population(population):
    """ 
    Creación de nuevas generaciones mediante reproducción. Para cada N habrá nuevos descendientes:
    - Se escoge a los padres al azar, 
    - los descendientes reciben un alelo de cada progenitor.
    """
    new_generation = []
    N = len(population)
    for i in range(N):
        # random integer between 0 and N-1
        dad = scipy.random.randint(N)
        mom = scipy.random.randint(N)
        # which chromosome comes from mom
        chr_mom = scipy.random.randint(2)
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom])
        #if offspring == ("a", "a"): 
          #next()
        new_generation.append(offspring)
    return new_generation