package exercicios_java;

import java.util.Scanner;

public class Ex37 {

	public static void main(String[] args) {
		// Exibir a tabuada dos valores de um a vinte, no intervalo de um a dez. Entre as tabuadas, solicitar que o usuário pressione uma tecla.
		
		
		Scanner ler = new Scanner (System.in);
		
		int i = 1, j = 1, t;
		
		while (i<=20){
			while (j<=10){
				t = i * j
				System.out.printf(" %d X %d = %d", i, j, t)
				j = j + 1
				i = i + i
			}
		}
		
		
		
		
		
		
		
	}

}
