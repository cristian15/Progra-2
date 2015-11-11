#include <stdlib.h>
#include <math.h>

 
int det();
int main(void)
 {
 	int i,j;
 	int  A[3][3]={ {1,-3,2}, {5,6,-1}, {4,-1,3} };
	int B[] = { {-3}, {13}, {8} }; 
 	
 	int tras[3][3], adj[3][3];		// matriz adjunta de la traspuesta y la traspuesta de A
	float invA[3][3], X[3];		// matriz inversa y la de resultados
	 
 	
 	// ====== Calcula la Matriz Traspuesta
 	for(i=0; i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			tras[i][j] = A[j][i];
		}
	} 
	// ==========================================
	
	// ========== Calcula la matriz adjunta de la traspuesta
	
	adj[0][0] = tras[1][1]*tras[2][2] - tras[2][1]*tras[1][2];
	adj[0][1] = -tras[0][1]*tras[2][2] - tras[2][1]*tras[0][2];
	adj[0][2] = tras[0][1]*tras[1][2] - tras[1][1]*tras[0][2];
	
	adj[1][0] = -tras[1][0]*tras[2][2] - tras[2][0]*tras[1][2];
	adj[1][1] = tras[0][0]*tras[2][2] - tras[2][0]*tras[0][2];
	adj[1][2] = -tras[0][0]*tras[1][2] - tras[1][0]*tras[0][2];
	
	adj[2][0] = tras[1][0]*tras[2][1] - tras[2][0]*tras[1][1];
	adj[2][1] = -tras[0][0]*tras[2][1] - tras[2][0]*tras[0][1];
	adj[2][2] = tras[0][0]*tras[1][1] - tras[1][0]*tras[0][1];
	
	// ===================================================
	
	
	// ====== Inversa de A	===========	
	double a = pow(det(A),-1);
	printf("1/det: %f\n", a);
 	for(i=0; i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			invA[i][j] = a*adj[i][j];
		}
	} 
	// ==========================================
	// ====== Calcula Matriz Resultados	===========	
	float r=0;
 	for(i=0; i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			r += invA[i][j] *(float) B[i];
			printf("%f\n",r);
		}
		X[i]=r;
		r=0;
	} 
	// ==========================================
	printf("\B  = \n");
	for(i=0; i<3;i++)
	{		
		printf("[%d]\n",B[i]);
	}	
	printf("A = \n");
	mostrar(A);
	
	printf("\nDeterminante de A: %d\n", det(A));
	
	printf("\nTraspuesta de A = \n");
	mostrar(tras);
	
	printf("\nAdjunta de A Traspuesta = \n");
	mostrar(adj);
	
	printf("\nInversa de A = \n");
	for(i=0; i<3;i++)
	{
		for(j=0;j<3;j++)
		{			
			printf("[%1.3f]\t", invA[i][j]);
		}
		printf("\n");
	}

	printf("\nResultado  = \n");
	for(i=0; i<3;i++)
	{		
		printf("[%1.2f]\n",X[i]);
	}	
 	return 0;
 }
 
 int det(int A[3][3]) // Determinante de Matriz 3x3
 { 	
 	return A[0][0]*( A[1][1]*A[2][2] - A[2][1]*A[1][2] ) - A[0][1]*( A[1][0]*A[2][2] - A[2][0]*A[1][2] ) + A[0][2]*( A[1][0]*A[2][1] - A[2][0]*A[1][1] );
 } 
 
 void  mostrar(int A[3][3])
 {
	int i, j;	
	
	for(i=0; i<3;i++)
	{
		for(j=0;j<3;j++)
		{			
			printf("[%d]\t", A[i][j]);
		}
		printf("\n");
	}
	
 }
 