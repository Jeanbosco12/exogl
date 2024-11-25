#Ecriture d'un fonction
def Hello(name):
    salut = "Hello "+ name;
    return salut;
def Logo():
    
    print('* * * *    *   * * * * *  *      *   *      *    * * * * *')
    print('*          *       *      *      *   *      *    *       *')
    print('*   ***    *       *      * *  * *   *      *    * * * **')
    print('*     *    *       *      *      *   *      *    *       *')
    print('* * * *    *       *      *      *   * *  * *    * * * * *')
        

Logo()
user = input("Entrer votre nom: ")
print(Hello(user))