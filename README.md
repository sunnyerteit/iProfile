# iProfile
A function that  can convert beam profiles to an equivalent I-profile, based on several  distinct properties. WIP

beamTest.py prints out data for I-profiles and associated properties. All of which are exported to file.csv. Feel free to change the range of the dimensions used in the profile generation.

example.py employs multivariate linear regression to fit a model based on the data in files.csv. At the moment it predicts properties based on dimensions, whereas in the future, the opposite will be true.

example2.py spits out dimensions based on properties. Mileage will vary. Should probably employ a randomforestgenerator. More to come.