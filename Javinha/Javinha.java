import javax.swing.JButton;
import javax.swing.*;
import java.awt.event.*;

class javinha {
    public static void main(String[] args) {

        JFrame Janela = new JFrame("HEART");


        final JTextField tf=new JTextField();
        tf.setBounds(50,50, 150,20);
        
        JButton botaofoda = new JButton("BOTÃO DO CARALHO");
        botaofoda.setBounds(100,100,180,30);
        

        botaofoda.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e){

                tf.setText("Procuro sexo.");
            }
        });
        Janela.add(botaofoda); Janela.add(tf);
        Janela.setSize(400,400);
        Janela.setLayout(null);
        Janela.setVisible(true);
    }
}