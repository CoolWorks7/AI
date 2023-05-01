import pgmpy.models
import pgmpy.inference


model = pgmpy.models.BayesianNetwork([('Burglary', 'Alarm'),
                                    ('Earthquake', 'Alarm'),
                                    ('Alarm', 'JohnCalls'),
                                    ('Alarm', 'MaryCalls')])

cpd_burglary = pgmpy.factors.discrete.TabularCPD('Burglary', 2, [[0.001], [0.999]])
cpd_earthquake = pgmpy.factors.discrete.TabularCPD('Earthquake', 2, [[0.002], [0.998]])
cpd_alarm = pgmpy.factors.discrete.TabularCPD('Alarm', 2, [[0.95, 0.94, 0.29, 0.001],
                                                           [0.05, 0.06, 0.71, 0.999]],
                                              evidence=['Burglary', 'Earthquake'],
                                              evidence_card=[2, 2])

cpd_john = pgmpy.factors.discrete.TabularCPD('JohnCalls', 2, [[0.90, 0.05],
                                                           [0.10, 0.95]],
                                              evidence=['Alarm'],
                                              evidence_card=[2])

cpd_mary = pgmpy.factors.discrete.TabularCPD('MaryCalls', 2, [[0.70, 0.01],
                                                           [0.30, 0.99]],
                                              evidence=['Alarm'],
                                              evidence_card=[2])

model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_john, cpd_mary)
model.check_model()
print('\n')

infer = pgmpy.inference.VariableElimination(model)

# Calculate the probability of a burglary if only John calls
evidence = {'JohnCalls': 1, 'MaryCalls': 0}
posterior_probability = infer.query(['Burglary'], evidence=evidence)
# Print posterior probability
print(f'Posterior probability of Burglary if JohnCalls({bool(evidence["JohnCalls"])}) and MaryCalls({bool(evidence["MaryCalls"])})')
print(posterior_probability)
print()

# Calculate the probability of a burglary if only Mary calls
evidence = {'JohnCalls': 0, 'MaryCalls': 1}
posterior_probability = infer.query(['Burglary'], evidence=evidence)
# Print posterior probability
print(f'Posterior probability of Burglary if JohnCalls({bool(evidence["JohnCalls"])}) and MaryCalls({bool(evidence["MaryCalls"])})')
print(posterior_probability)
print()

# Calculate the probability of a burglary if John and Mary calls
evidence = {'JohnCalls': 1, 'MaryCalls': 1}
posterior_probability = infer.query(['Burglary'], evidence=evidence)
# Print posterior probability
print(f'Posterior probability of Burglary if JohnCalls({bool(evidence["JohnCalls"])}) and MaryCalls({bool(evidence["MaryCalls"])})')
print(posterior_probability)
print()

# Calculate the probability of a Burglary if no one calls
evidence = {'JohnCalls': 0, 'MaryCalls': 0}
posterior_probability = infer.query(['Burglary'], evidence=evidence)
# Print posterior probability
print(f'Posterior probability of Burglary if JohnCalls({bool(evidence["JohnCalls"])}) and MaryCalls({bool(evidence["MaryCalls"])})')
print(posterior_probability)
print()
