package com.tobe.sql;

import com.tobe.sql.SqlBaseBaseVisitor;
import com.tobe.sql.SqlBaseParser.*;

public class SimpleSqlVisitor extends SqlBaseBaseVisitor {

    @Override
    public String visitFromClause(SqlBaseParser.FromClauseContext ctx) {
        String tableName = visitRelation(ctx.relation(0));
        System.out.println("SQL table name: " + tableName);
        return tableName;
    }

    @Override
    public String visitRelation(SqlBaseParser.RelationContext ctx) {
        if (ctx.relationPrimary() instanceof TableNameContext) {
            return visitTableName((TableNameContext)ctx.relationPrimary());
        }
        return "";
    }

    @Override
    public String visitTableName(SqlBaseParser.TableNameContext ctx) {
        return visitTableIdentifier(ctx.tableIdentifier());
    }

    @Override
    public String visitTableIdentifier(SqlBaseParser.TableIdentifierContext ctx) {
        return ctx.getChild(0).getText();
    }

}
