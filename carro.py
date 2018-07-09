import sys
import time

def gale():
	x = int(time.strftime("%H%M%S%S"))
	#print(x)
	ale=0.0
	r = ([0,0,0,0,0,0,0,0])
	factor =([10000000,1000000,100000,10000,1000,100,10,1])

	for i in range(1):
		#print (x);
		n=x*x;
	
		#print (n);
		r[0] = int(n/10000000);
		
		n=n-(r[0]*factor[0]);
		#print (n)
		r[1] = int(n/1000000);	
		n=n-(r[1]*factor[1]);	
		r[2] = int(n/100000);
		n=n-(r[2]*factor[2]);
		r[3] =int( n/10000);
		n=n-(r[3]*factor[3]);
		r[4] =int(n/1000);
		n=n-(r[4]*factor[4]);
		r[5] = int(n/100);
		n=n-(r[5]*factor[5]);
		r[6] = int(n/10);
		n=n-(r[6]*factor[6]);
		r[7] = int(n/1);
		#print(r);
		ni=2
		for j in range(2,6):
			ale=ale+(r[j]*factor[j])
			#print("factorp: ",r[j]*factor[j]);	
		ale=ale/factor[5]
		#print("numero aleatorio:",ale)
		x=ale
		n=0;
		ale=0;
		print("dato ",i+1)
		print (x%10)

def main():

	print("En la simulacion de una auto\nesperamos determinar el tiempo de llegada optimo")
	gale()
	print("tomamos en cuenta como variables aleatorias discretas, el numero de baches (1) en el camino y el de personas (2) en el auto")
    




if __name__ == "__main__":main()


