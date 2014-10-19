def energy(density, coeff=1.0):
  """ Energy associated with the diffusion model

      Parameters
      ----------

      density: array of positive integers
          Number of particles at each position i in the array
      coeff: float
          Diffusion coefficient.
  """
  
  # #Initialise e (before using  e +=)
  # e = 0
  
  # #loop over all values in array
  # for n in density:
    # e += (coeff / 2) * n * (n + 1)
  # return e

  #Improved attempt
  
  #Imports
  from numpy import array, sum
  
  #Assign density list to an numpy array
  density = array(density)
  
  #Main code in return 
  return coeff * 0.5 * sum(density * (density - 1))
  