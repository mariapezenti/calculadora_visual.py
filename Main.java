public class Main {
    public static void main(String[]args) {
        Funcionario funcionario1 = new Funcionario ("Luiza", "Analista", 4000);
        Funcionario funcionario2 = new Funcionario ("Maria", "Programadora", 5500);
        Funcionario funcionario3 = new Funcionario ("Lucas", "Desenvolvedor", 5000);

      System.out.println("Funcionário 1");
        System.out.println("Nome" + funcionario1.nome);
        System.out.println("Cargo" + funcionario1.cargo);
        System.out.println("Salário" + funcionario1.salario);

    System.out.println();

        System.out.println("Funcionário 2");
        System.out.println("Nome" + funcionario2.nome);
        System.out.println("Cargo" + funcionario2.cargo);
        System.out.println("Salário" + funcionario2.salario);

      System.out.println();

        System.out.println("Funcionário 3");
        System.out.println("Nome" + funcionario3.nome);
        System.out.println("Cargo" + funcionario3.cargo);
        System.out.println("Salário" + funcionario3.salario);
    
    }
}

