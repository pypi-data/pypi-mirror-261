import logging
import os
from datetime import datetime

import xlsxwriter as xl
from sqlalchemy import text


class EaseExcel():
    """
    A class for building Excel files from cursor data.

    Args:
        cursor (object): The cursor object containing the data.
        filename (str): The filename for the Excel file to be created.
    """

    def __init__(
            self,
            sqlalchemy_engine: object,
            SQL_query: str,
            file_name: str = None,
            file_path: str = None
    ) -> None:
        """
        sqlalchemy_engine (object): Sqlalchemy engine object
        SQL_query (str): Query to run
        file_name (str): file name is None provided default will we used
        file_path (str): file path if none is provided use current directory as default

        """ # noqa

        self.sqlalchemy_conn = sqlalchemy_engine
        self.query = SQL_query
        self.file_name = file_name
        self.file_path = file_path

        # create a file name if filename is empty
        if self.file_name is None:
            current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.file_name = 'Ease_excel_'+str(current_time)

        # Default file path if file path is empty
        if self.file_path is None:
            self.file_path = os.getcwd()

        # building final path
        self.file_org_path = os.path.join(self.file_path, self.file_name)

    # Get the data from provided query
    @staticmethod
    async def execute_the_query(
        sqlalchemy_engine: object,
        sql_query: str
    ):
        """
        Execute the the privided sql query and return cursor

        Args:
            sqlalchemy_engine (object): SQl alchemy engine object for building connection
            sql_query (str): Query to run
        
        """# noqa
        conn = sqlalchemy_engine.connect()
        return conn.execute(text(sql_query))

    # Write the data to excel file
    @staticmethod
    async def build_excel(
        cursor: object,
        file_path: str
    ) -> object:
        """
        Builds an Excel file from the cursor data.

        Args:
            cursor (object): The cursor object containing the data.
            filename (str): The filename for the Excel file to be created.

        Returns:
            cursor (object): Return the cursor object after execution
        """

        workbook = xl.Workbook(str(file_path)+'.xlsx', {
            'default_date_format': 'dd/mm/yy',
            'remove_timezone': 'true',
            'wrap_text': True})

        # Get the active worksheet
        worksheet = workbook.add_worksheet()
        header_format = workbook.add_format(
            {'bold': True,
             'font_color': 'black'}
            )

        # Get the headers of the data
        headers = [column for column in cursor.keys()]

        # Write the headers to the first row of the worksheet
        for col_num, header in enumerate(headers, 0):
            worksheet.write(
                0,
                col_num, header, header_format)

        # Write the remaining data to the worksheet
        for row_num, row in enumerate(cursor, 1):
            for col_num, cell_value in enumerate(row, 0):
                worksheet.write(row_num, col_num, cell_value)

        workbook.close()

    # call the excel creater and data extractor functions
    async def build(self):
        """
        Builds the excel file
        """
        try:
            cursor = await self.execute_the_query(
                self.sqlalchemy_conn,
                self.query
            )
            await self.build_excel(cursor, self.file_org_path)

        except Exception as e:
            logging.exception('Error creating file: %s', str(e))
            return e
