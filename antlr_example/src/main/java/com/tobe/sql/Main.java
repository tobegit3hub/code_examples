package com.tobe.sql;

import com.tobe.sql.*;
import org.antlr.v4.runtime.*;

public class Main {

    public static void main(String[] argv) {
        String sqlText = "SELECT C1, C2 FROM T1";

        MySqlVisitor visitor = new MySqlVisitor();
        SqlBaseLexer lexer = new SqlBaseLexer(CharStreams.fromString(sqlText));
        CommonTokenStream tokenStream = new CommonTokenStream(lexer);
        SqlBaseParser parser = new SqlBaseParser(tokenStream);
        MyErrorListener errorListener = new MyErrorListener();
        parser.addErrorListener(errorListener);

        parser.singleStatement().accept(visitor);
    }

}