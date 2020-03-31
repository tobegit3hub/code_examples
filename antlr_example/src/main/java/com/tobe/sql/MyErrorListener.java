package com.tobe.sql;

import org.antlr.v4.runtime.*;

public class MyErrorListener extends BaseErrorListener {

    @Override
    public void syntaxError(Recognizer<?, ?> recognizer, Object offendingSymbol, int line,
            int charPositionInLine, String msg, RecognitionException e) {

        // super.syntaxError(recognizer, offendingSymbol, line, charPositionInLine, msg, e);
        System.out.println("Get SQL syntax error");
    }

}
