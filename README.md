# find-the-shortest-possible-route-with-distance
Let, Rabat = A, Sueca = B, Rudow = C, Mosu = D, Le Plessis Trevise = E, Kang Dong =F, Nezahualcóyotl =G, Lindenwold = H, Queanbeyan = I, Saint Chamond = J, Cheektowaga = K, Tirupati = L, Snezhinsk = M, Glazov = N, Gaoyou = O, Nola = P, Rutigliano = Q, Colombo = R, Meckenheim = S, Hamburg = T

# Graph : 

        A ----1063----> B ----2656----> C ----1352----> D ----1841----> E ----61----> F ----1634----> G ----151----> H ----285----> I  
        ^                                                                                                                           |             
        |                                                                                                                           |              
        30                                                                                                                          146            
        |                                                                                                                           |             
        |                                                                                                                           |          
        T                                                                                                                           J
        ^                                                                                                                           | 
        |                                                                                                                           |
        502                                                                                                                         11
        |                                                                                                                           | 
        |                                                                                                                           |   
        S <----244----- R <----105---- Q <----63---- P <----6999---- O <----97---- N <----2524---- M <----2547---- L <----380------ k
                    
                                                                                                                                                                                    ---> This graph is a  Hamiltonian circuits. Circuit that visits every vertex once with no repeats. Being a circuit, it start and end at the same vertex.
                                                                                                                                                                                    ---> Also This graph is cyclic. Whatever we consider the starting point the distance will be same and return a single route
                                                                                                                                                                                    ---> I consider A as starting point. 
                                                                                                                                                                                             path : A - B - C - D - E - F - G - H - I - J - K - L - M - N - O - P - Q - R - T - A 
                                                                                                                                                                                             total Distance: 22721
                                                                                                                                                                                             
                                                                                                                                        
