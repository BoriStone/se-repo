package com.company;

import java.util.Scanner;
import java.util.Timer;

class Cat extends Pet {
    Cat(String name) {
        hungry = 100;
        energy = 100;
        mood = 50;
        this.name = name;
        in = new Scanner(System.in);
        time = new Timer();
        time.scheduleAtFixedRate(task,1000,2000);
    }

    public void lifecat(){
        boolean catty = true;
        while (catty == true){
            System.out.println("Выберите действие с вашим питомцем: \n 1 - Покормить кормом \n 2 - Покормить капустой \n 3 - Наказать за обоссаные тапки! \n 4 - положить спать \n 5 - Показать состояние питомца (Подсказака: проверяйте чаще) \n 6 - Не бить питомца \n 7 - Выход из игры");
            int nyam;
            nyam = in.nextInt();
            switch(nyam){
                case 1 :
                    eatFeed();
                    break;
                case 2 :
                    eatCabbage();
                    break;
                case 3 :
                    kickOff();
                    break;
                case 4 :
                    sleep();
                    break;
                case 5 :
                    System.out.println("Энергия " + name + ":  " + energy);
                    System.out.println("Сытость " + name + ":  " + hungry);
                    System.out.println("Настроение " + name + ":  " + mood);
                    break;
                case 6 :
                    mood+=10;
                    System.out.println(name + " вам очень благодарен(а)");
                    System.out.println("Настроение: " + mood);
                    break;
                case 7 :
                    System.exit(0);
                    break;
                default :
                    System.out.println("Ошибка!");
                    break;
            }
        }
    }
}
