package com.example.rdx.a5andb3;

import android.content.SharedPreferences;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    Button sin_b;
    Button cos_b;
    Button tan_b;
    Button sqrt_b;
    Button add_b;
    Button sub_b;
    Button mul_b;
    Button div_b;
    Button save_b;
    Button recall_b;
    EditText num1_field;
    EditText num2_field;
    TextView resultView;

    public static double add(double a, double b){
        return a + b;
    }

    class UnaryOp implements View.OnClickListener{
        @Override
        public void onClick(View v) {
            String ip1 = num1_field.getText().toString();
            double num1 = Double.parseDouble(ip1);
            String op = ((Button)v).getText().toString();
            double res = 0;
            switch (op){
                case "sin":{
                    res = Math.sin(Math.toRadians(num1));
                    break;
                }
                case "cos":{
                    res = Math.cos(Math.toRadians(num1));
                    break;
                }
                case "tan":{
                    res = Math.tan(Math.toRadians(num1));
                    break;
                }
                case "sqrt":{
                    res = Math.sqrt(num1);
                    break;
                }
            }
            resultView.setText(Double.toString(res));
        }
    }

    class BinaryOp implements View.OnClickListener{
        @Override
        public void onClick(View v) {
            String ip1 = num1_field.getText().toString();
            double num1 = Double.parseDouble(ip1);
            String ip2 = num2_field.getText().toString();
            double num2 = Double.parseDouble(ip2);
            String op = ((Button)v).getText().toString();
            double res = 0;
            switch (op){
                case "+":{
                    res = num1 + num2;
                    break;
                }
                case "-":{
                    res = num1 - num2;
                    break;
                }
                case "*":{
                    res = num1 * num2;
                    break;
                }
                case "/":{
                    res = num1 / num2;
                    break;
                }
            }
            resultView.setText(Double.toString(res));
        }
    }

    class Save implements View.OnClickListener{
        @Override
        public void onClick(View v) {
            String res = resultView.getText().toString();
            if(!res.isEmpty()){
                SharedPreferences.Editor editor = getSharedPreferences("storageFile", MODE_PRIVATE).edit();
                editor.putString("result", res);
                editor.commit();
            }
        }
    }

    class  Recall implements View.OnClickListener{
        @Override
        public void onClick(View v) {
            SharedPreferences preferences = getSharedPreferences("storageFile", MODE_PRIVATE);
            if(preferences.contains("result")){
                String res = preferences.getString("result", "");
                resultView.setText(res);
            }
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activitymain);

        UnaryOp unaryOp = new UnaryOp();
        BinaryOp binaryOp = new BinaryOp();
        Save save = new Save();
        Recall recall = new Recall();

        sin_b = (Button)findViewById(R.id.button_sin);
        sin_b.setOnClickListener(unaryOp);

        cos_b = (Button)findViewById(R.id.button_cos);
        cos_b.setOnClickListener(unaryOp);

        tan_b = (Button)findViewById(R.id.button_tan);
        tan_b.setOnClickListener(unaryOp);

        sqrt_b = (Button)findViewById(R.id.button_sqrt);
        sqrt_b.setOnClickListener(unaryOp);

        add_b = (Button)findViewById(R.id.button_add);
        add_b.setOnClickListener(binaryOp);

        sub_b = (Button)findViewById(R.id.button_sub);
        sub_b.setOnClickListener(binaryOp);

        mul_b = (Button)findViewById(R.id.button_mul);
        mul_b.setOnClickListener(binaryOp);

        div_b = (Button)findViewById(R.id.button_div);
        div_b.setOnClickListener(binaryOp);

        save_b = (Button)findViewById(R.id.button_save);
        save_b.setOnClickListener(save);

        recall_b = (Button)findViewById(R.id.button_recall);
        recall_b.setOnClickListener(recall);

        num1_field = (EditText)findViewById(R.id.num1_field);
        num2_field = (EditText)findViewById(R.id.num2_field);
        resultView = (TextView)findViewById(R.id.resultView);
    }
}
