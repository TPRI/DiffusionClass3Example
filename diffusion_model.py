def energy(density, coeff=1.0):
  """ Energy associated with the diffusion model

      Parameters
      ----------

      density: array of positive integers
          Number of particles at each position i in the array
      coeff: float
          Diffusion coefficient.
  """
  e = 0
  
  for n in density:
    e += (coeff / 2) * n * (n + 1)
  return e
