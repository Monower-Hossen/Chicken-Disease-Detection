# main.py
import sys

try:
    from chicken_classifier import logger
    from chicken_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
    from chicken_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
    from chicken_classifier.pipeline.stage_03_model_training import ModelTrainingPipeline
    from chicken_classifier.pipeline.stage_04_evaluation import EvaluationPipeline
except KeyboardInterrupt:
    print("\nInterrupted during initialization. Exiting...")
    sys.exit(0)

if __name__ == "__main__":

    # Stage 01: Data Ingestion
    try:
        STAGE_NAME = "Data Ingestion stage"
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except KeyboardInterrupt:
        logger.info("Process interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        logger.exception(e)
        raise e

    # Stage 02: Prepare Base Model
    try:
        STAGE_NAME = "Prepare base model"
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except KeyboardInterrupt:
        logger.info("Process interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        logger.exception(e)
        raise e

    # Stage 03: Training
    try:
        STAGE_NAME = "Training"
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_training = ModelTrainingPipeline()
        model_training.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except KeyboardInterrupt:
        logger.info("Process interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        logger.exception(e)
        raise e

    # Stage 04: Evaluation
    try:
        STAGE_NAME = "Evaluation"
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_evaluation = EvaluationPipeline()
        model_evaluation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except KeyboardInterrupt:
        logger.info("Process interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        logger.exception(e)
        raise e