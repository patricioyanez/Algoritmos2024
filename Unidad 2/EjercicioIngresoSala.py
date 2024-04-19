## ejercicios:
# para controlar la entrada a la sala de clases
# preguntar al alumno si esta matriculado
# y si inscribio en la asignatura

matriculado = input("Ud esta matriculado?: 1.-Si / 2.-No ")
inscrito = input("Ud esta inscrito?: 1.-Si / 2.-No ")

if matriculado == "1" and  inscrito == "1":
    print ("Bienvenido, puede entrar")
else:
    print("No puede entrar. :(")
    