import os

from pydantic.v1.schema import get_flat_models_from_model

import funkcion.slovo


def IS():
    base = os.path.dirname(__file__)
    base = os.path.join(base, "IS")
    # print(base)
    paths = os.path.join(base, "IS.txt")
    name="Indukčné snímače"
    downlode=os.path.join(base, "IS.docx")

    # print(paths)
    funkcion.slovo.main(base, paths,downlode,name)


IS()
