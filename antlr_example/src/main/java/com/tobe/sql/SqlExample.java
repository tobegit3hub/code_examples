package com.tobe.sql;

import org.antlr.v4.runtime.*;

public class SqlExample {

    public static void main(String[] argv) {
        String sqlText = "SELECT C1, C2 FROM T1";

        SimpleSqlVisitor visitor = new SimpleSqlVisitor();
        SqlBaseLexer lexer = new SqlBaseLexer(CharStreams.fromString(sqlText));
        CommonTokenStream tokenStream = new CommonTokenStream(lexer);
        SqlBaseParser parser = new SqlBaseParser(tokenStream);
        SimpleErrorListener errorListener = new SimpleErrorListener();
        parser.addErrorListener(errorListener);

        parser.singleStatement().accept(visitor);
    }

}