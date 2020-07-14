
def create_tables(metadata):
    metadata.create_all()


def drop_tables(metadata):
    metadata.drop_all()
