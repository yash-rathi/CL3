package com.example.rdx.a5andb3;

import org.junit.Test;

import static org.junit.Assert.*;

public class MainActivityTest {
    @Test
    public void test_add(){
        double x = MainActivity.add(20, 20.5);
        assertEquals(x, 40.5, 0);
    }
}