package com.company;
import java.util.Scanner;

public class Main {

    public static void general(){
        System.out.println("Добро пожаловать в игру!");
        String name;
        Scanner in = new Scanner(System.in);
        boolean cik = true;
        while(cik == true){
            System.out.println("Сделайте свой выбор: \n 1 - КОТ \n 2 - СОБАКА \n 3 - Выход из игры!" );
            int choose;
            choose = in.nextInt();
            switch(choose){
                case 1 :
                    System.out.println("Введите имя питомца: ");
                    name = in.next();
                    Cat obj = new Cat(name);
                    obj.lifecat();
                    cik = false;
                    break;
                case 2 :
                    System.out.println("Введите имя питомца: ");
                    name = in.next();
                    Dog obje = new Dog(name);
                    obje.lifedog();
                    cik = false;
                    break;
                case 3 :
                    System.exit(0);
                    break;
                default:
                    System.out.println("Ошибка!");
                    break;
            }
        }
    }
    public static void main(String[] args) {
        System.out.println("╔════╦══╦╗──╔╦══╦═══╦╗╔╦══╦══╦══╗\n" +
                "╚═╗╔═╣╔╗║║──║║╔╗║╔══╣║║║╔═╣╔═╩╗╔╝\n" +
                "──║║─║╚╝║╚╗╔╝║║║║║╔═╣║║║║─║║──║║\n" +
                "──║║─║╔╗║╔╗╔╗║║║║║╚╗║║║║║─║║──║║\n" +
                "──║║─║║║║║╚╝║║╚╝║╚═╝║╚╝║╚═╣╚═╦╝╚╗\n" +
                "──╚╝─╚╝╚╩╝──╚╩══╩═══╩══╩══╩══╩══╝");
        System.out.println("-------------------------------------------------------------------------");
        general();
    }
}
