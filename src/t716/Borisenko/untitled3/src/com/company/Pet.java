package com.company;

import java.util.Scanner;
import java.util.Timer;
import java.util.TimerTask;

class Pet{
        protected String name;
        protected int hungry;
        protected int energy;
        protected int mood;
        Scanner in;
        Timer time;
        TimerTask task = new TimerTask() {
            @Override
            public void run() {
                if (hungry>0){
                    hungry-=5;
                    if (hungry<=20){
                        if (energy>0){
                            energy-=5;
                        }
                    }
                }
                else {
                    if (energy>0){
                        energy-=5;
                    }
                    else{
                        System.out.println("----------------------------------------------------------------------------\n" +
                                "ПОТРАЧЕНО \n" + "(Умер от голода и потери сил) \n" +  "Начните заново!\n" +
                                "----------------------------------------------------------------------------");
                        Main.general();
                    }
                }
            }
        };

        public void eatFeed(){

            if (hungry >= 100){
                System.out.println("Корм сейчас не к месту! ");
            }
            else {
                hungry+=20;
                if (hungry>100){
                    int tempp = hungry - 100;
                    hungry -= tempp;
                }
                System.out.println("Питомец доволен! \n" +
                        "Сытость: " + hungry );
            }
        }

        public void sleep(){
            int prov = energy+40;
            if (prov>100){
                System.out.println("Ваш(а) " + name + " не хочет спать");
            }
            else{
                energy+=40;
                mood+=10;
                System.out.println(name + " поспал(a) \n" +
                        "Энергия: " + energy);
                System.out.println("Настроение: " + mood);
            }
        }

        public void eatFat(){
            int temp = 100 - energy;
            int temp1 = 100 - hungry;
            int temp2 = 100 - mood;
            if (hungry >= 100){
                System.out.println("Сало сейчас не к месту! ");
            }
            else {
                hungry+=temp1;
                energy+=temp;
                mood+=temp2;
                System.out.println("Питомец доволен! \n" +
                        "Сытость: " + hungry );
                System.out.println("Запасы сил: " + energy);
                System.out.println("Настроение: " + mood);
            }
        }

        public void eatCabbage(){
            if (hungry>=100){
                System.out.println("Ваш питомец явно не голоден сейчас!");
            }
            else {
                hungry+=10;
                System.out.println(name + " покушал(a) \n" +
                        "Сытость: " + hungry);
            }
        }

        public void kickOff(){
            energy-=10;
            mood-=4;
            if (energy<=0){
                System.out.println("----------------------------------------------------------------------------\n" + "ПОТРАЧЕНО  \n" + "Начните заново! \n" + "----------------------------------------------------------------------------");
                Main.general();
            }
            else{
                System.out.println(name + " осознал(a) свою вину :с \n"+
                        "Силы питомца: " + energy);
                System.out.println("Настроение: " + mood);
            }
        }
    }

