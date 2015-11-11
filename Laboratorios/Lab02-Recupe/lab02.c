#include <stdio.h>
#include <stdlib.h>

void compara();
int main(int argc, char *argv[])
{
	char Data[6] = {10, -15, -125, 65, 45, -89};
	FILE *pF = fopen("char.bin","wb");
	fwrite(&Data, sizeof(Data), 1, pF);
	printf("%d\n",Data[0]);
	fclose(pF);
	system("PAUSE");
	
	compara(Data);
	return 0;
}

void compara(char D[])
{
	FILE *hF = fopen("char.bin","rb");		// abre el archivo en modo lectura binaria
	
	unsigned char buffer[6];		// 
	
	fread(buffer, sizeof(buffer), 1, hF);		// lee el archivo y lo pasa a buffer
	
	int i;
	for(i=0; i<6;i++)		// muestra el buffer a un lado del arreglo pasado
	{
	
		printf("Dato Hex char.bin: %x\t Dato Data[]: %d\n ", buffer[i], D[i]);
	}
	
	
}
