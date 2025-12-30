import py4j.GatewayServer;

public class server {

    // Método que o Python vai chamar enviando um valor
    public String saudacao(String nome) {
        return "Olá, " + nome + "! Eu sou o Java e recebi seu valor.";
    }

    public static void main(String[] args) {
        server aplicacao = new server();
        // Inicia o servidor Gateway na porta padrão (25333)
        GatewayServer servidor = new GatewayServer(aplicacao);
        servidor.start();
        System.out.println("Servidor Gateway Java iniciado com sucesso!");
    }
}
