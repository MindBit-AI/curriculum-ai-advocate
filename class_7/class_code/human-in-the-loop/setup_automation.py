from langsmith import Client

client = Client()

# Create automation rule to collect feedback
client.create_project_rule(
    project_name="customer_service_plans",
    rule_name="collect_feedback",
    filter_expression="has_feedback:true",
    action_type="add_to_dataset",
    action_config={
        "dataset_name": "customer_service_plans",
        "use_corrections": True
    }
) 