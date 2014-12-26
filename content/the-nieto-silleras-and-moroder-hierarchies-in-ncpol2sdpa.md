Title: The Nieto-Silleras and Moroder hierarchies in Ncpol2sdpa
Date: 2014-11-27 10:44
Author: Peter
Category: Semidefinite programming
Tags: Noncommutative polynomials, Python, Quantum information theory, Semidefinite programming, SymPy
Slug: the-nieto-silleras-and-moroder-hierarchies-in-ncpol2sdpa
Summary: Generating the semidefinite programming relaxation of polynomial optimization problems of noncommuting variables using the Nieto-Silleras and the Moroder hierarchies.

Some alternatives to the NPA hierarchy ([Pironio et al., 2010](#pironio2010convergent)) were published recently. One of the new
approaches takes all joint probabilities into consideration when looking
for a maximum guessing probability, and not just the ones included in a
particular Bell inequality ([Nieto-Silleras et al., 2014](#nieto-silleras2014using), [Bancal et al., 2014](#bancal2014more)). We refer to this type as the Nieto-Silleras hierarchy.

The other extension consider a tensor product structure between the parties in a two-party Bell experiment ([Moroder et al., 2013](#moroder2013device)). This structure allows imposing further
constraints that are not possible in the NPA hierarchy, such as the
positivity of the partial transpose of the moment matrix. We refer to
this as the Moroder hierarchy.

[Ncpol2sdpa](http://peterwittek.github.io/ncpol2sdpa/) was recently
extended to generate these two types of hierarchies, and the subsequent
sections give an example to each. We assume that Ncpol2sdpa version 1.5
and its dependencies are installed, [QuTiP](http://qutip.org/) is
available, and the default solver, SDPA, is also operational.

Nieto-Silleras hierarchy
------------------------

To deal with the joint probabilities necessary for setting constraints,
we also rely on QuTiP ([Johansson et al., 2013](#johansson2013qutip)).
First we need to import some functions:

    :::python
    from math import sqrt
    from qutip import tensor, basis, sigmax, sigmay, expect, qeye
    from ncpol2sdpa import SdpRelaxation, flatten, solve_sdp,   
                          generate_measurements,   
                          projective_measurement_constraints

We will work in a CHSH scenario where we are trying to find the maximum
guessing probability of the first projector of Alice's first
measurement. We generate the joint probability distribution on the
maximally entangled state with the measurements that give the maximum
quantum violation of the CHSH inequality:

    :::python
    def joint_probabilities():
        psi = (tensor(basis(2,0),basis(2,0)) + 
               tensor(basis(2,1),basis(2,1))).unit()
        A_0 = sigmax()
        A_1 = sigmay()
        B_0 = (-sigmay()+sigmax())/sqrt(2)
        B_1 = (sigmay()+sigmax())/sqrt(2)

        A_00 = (qeye(2) + A_0)/2
        A_10 = (qeye(2) + A_1)/2
        B_00 = (qeye(2) + B_0)/2
        B_10 = (qeye(2) + B_1)/2

        p=[]
        p.append(expect(tensor(A_00, qeye(2)), psi))
        p.append(expect(tensor(A_10, qeye(2)), psi))
        p.append(expect(tensor(qeye(2), B_00), psi))
        p.append(expect(tensor(qeye(2), B_10), psi))

        p.append(expect(tensor(A_00, B_00), psi))
        p.append(expect(tensor(A_00, B_10), psi))
        p.append(expect(tensor(A_10, B_00), psi))
        p.append(expect(tensor(A_10, B_10), psi))
        return p

Next we need the basic configuration of the projectors. We also set the
level of the SDP relaxation and the objective.

    :::python
    level = 1
    A_configuration = [2, 2]
    B_configuration = [2, 2]
    P_A = generate_measurements(A_configuration, 'P_A')
    P_B = generate_measurements(B_configuration, 'P_B')
    monomial_substitutions = projective_measurement_constraints(
        P_A, P_B)
    objective = -P_A[0][0]

We must define further constraints, namely that the joint probabilities
must match:

    :::python
    probabilities = joint_probabilities()
    equalities = []
    k=0
    # We impose the constraints of the Nieto-Silleras formulation 
    # using the joint probabilities. Marginals go first.
    for i in range(len(A_configuration)):
        equalities.append(P_A[i][0]-probabilities[k])
        k += 1
    for i in range(len(B_configuration)):
        equalities.append(P_B[i][0]-probabilities[k])
        k += 1
    for i in range(len(A_configuration)):
        for j in range(len(B_configuration)):
            equalities.append(P_A[i][0]*P_B[j][0]-probabilities[k])
            k += 1

From here, obtaining the SDP relaxation and solving it is trivial:

    :::python
    sdpRelaxation = SdpRelaxation([flatten([P_A, P_B])], verbose=2,
                                   hierarchy="nieto-silleras")
    sdpRelaxation.get_relaxation(objective, [], equalities,
                                 monomial_substitutions, level)

    print(solve_sdp(sdpRelaxation))

    Number of SDP variables: 15
    Generating moment matrix...
    Reduced number of SDP variables: 11
    Processing 16 inequalities...
    (-0.5000000504870096, -0.5000001112451216)


Moroder hierarchy
-----------------

This type of hierarchy allows for a wider range of constraints of the
optimization problems, including ones that are not of polynomial form.
These constraints are hard to impose using SymPy and the sparse
structures in Ncpol2Sdpa. For this reason, we separate two steps:
generating the SDP and post-processing the SDP to impose extra
constraints. This second step can be done in MATLAB, for instance.

We need to import a slightly different set of functions:

    :::python
    from ncpol2sdpa import SdpRelaxation, flatten, write_to_sdpa,   
                          generate_measurements,   
                          projective_measurement_constraints,   
                          define_objective_with_I

Then we set up the problem with specifically with the CHSH inequality in
the probability picture as the objective function:

    :::python
    level = 1
    A_configuration = [2, 2]
    B_configuration = [2, 2]
    I = [[ 0,   -1,    0 ],
         [-1,    1,    1 ], 
         [ 0,    1,   -1 ]]
    A = generate_measurements(A_configuration, 'A')
    B = generate_measurements(B_configuration, 'B')
    monomial_substitutions = projective_measurement_constraints(A, B)
    objective = define_objective_with_I(I, A, B)

We obtain the relaxation and write it to a sparse SDPA file:

    :::python
    sdpRelaxation = SdpRelaxation([flatten(A), flatten(B)], verbose=2,
                                   hierarchy="moroder")
    sdpRelaxation.get_relaxation(objective, [], [],
                                 monomial_substitutions, level)
    write_to_sdpa(sdpRelaxation, "chsh-moroder.dat-s")

    Number of SDP variables: 44
    Generating moment matrix...
    Reduced number of SDP variables: 18
    Processing 0 inequalities...

From here, processing switches to MATLAB. We can read the SDPA file with
[SeDuMi](http://sedumi.ie.lehigh.edu/) or
[Yalmip](http://users.isy.liu.se/johanl/yalmip/), for instance. Yalmip
gives more flexibility, so we work with that. The default function for
loading is called loadsdpafile. We modify this to return the moment
matrix itself:

    :::matlab
    function [F,h,momentmatrix] = loadsdpafilehacked(varargin)

    filename = varargin{1};
    % Does the file exist
    if ~exist(filename)
        filename = [filename '.dat-s'];
        if ~exist(filename)
            error(['No such file.']);
        end
    end
        
    % Load using SeDuMi
    try
        [At,b,c,K] = fromsdpa(filename);
    catch
        error('LOADSDPAFILE currently requires SeDuMi to be installed');
    end

    nvars = length(b);
    x = sdpvar(nvars,1);

    F = ([]);
    top = 1;
    if isfield(K,'l')
        if K.l(1)>0
            X = c(top:top+K.l-1)-At(top:top+K.l-1,:)*x;
            F = F + (X(:)>=0);
            top = top + K.l;
        end
    end

    first=0;
    if isfield(K,'s')
        if K.s(1)>0
            for i = 1:length(K.s)
                [ix,iy,iv] = find([c(top:top+K.s(i)^2-1) At(top:top+K.s(i)^2-1,:)]);
                off = (ix-1)/(K.s(i)+1);
                if all(off == round(off))
                    X = c(top:top+K.s(i)^2-1)-At(top:top+K.s(i)^2-1,:)*x;
                    F = F + (diag(reshape(X,K.s(i),K.s(i))) >= 0);
                    if first==0
                        momentmatrix=diag(reshape(X,K.s(i),K.s(i)));
                    end
                    top = top + K.s(i)^2;
                else
                    X = c(top:top+K.s(i)^2-1)-At(top:top+K.s(i)^2-1,:)*x;
                    whatever = c(top:top+K.s(i)^2-1)
                    F = F + (reshape(X,K.s(i),K.s(i)) >= 0);
                    if first==0
                        momentmatrix=reshape(X,K.s(i),K.s(i));
                    end
                    top = top + K.s(i)^2;
                end
            end
            first=1;
        end
    end
    h = -b'*x;

Using this modified function, we can perform arbitrary postprocessing on
the moment matrix, for instance, imposing the PPT condition:

    :::matlab
    [F,h,momentmatrix]=loadsdpafilehacked('chsh-moroder.dat-s');
    F = F + (PartialTranspose(momentmatrix>=0)
    optimize(F,h)

References
==========

<a name="bancal2014more"></a>Bancal, J.-D.; Sheridan, L. & Scarani, V.
[More randomness from the same data](http://dx.doi.org/10.1088/1367-2630/16/3/033011). New Journal of
Physics, 2014, 16, pp. 033011.

<a name="johansson2013qutip"></a>Johansson, J.R.; Nation, P.D. & Nori,
F. [QuTiP 2: A Python framework for the dynamics of open quantum systems](http://dx.doi.org/10.1016/j.cpc.2012.11.019). Computer Physics
Communications, 2013, 184, pp. 1234--1240.

<a name="moroder2013device"></a>Moroder, T.; Bancal, J.-D.; Liang,
Y.-C.; Hofmann, M. & Gühne, O. [Device-independent entanglement quantification and related applications](http://dx.doi.org/10.1103/PhysRevLett.111.030501). Physics
Review Letters, American Physical Society, 2013, 111, pp. 030501.

<a name="nieto-silleras2014using"></a>Nieto-Silleras, O.; Pironio, S. &
Silman, J. [Using complete measurement statistics for optimal device-independent randomness evaluation](http://dx.doi.org/10.1088/1367-2630/16/1/013035). New
Journal of Physics, 2014, 16, pp. 013035.

<a name="pironio2010convergent"></a>Pironio, S.; Navascués, M. & Acín,
A. [Convergent relaxations of polynomial optimization problems with noncommuting variables](http://arxiv.org/abs/0903.4368). *SIAM Journal
on Optimization*, 2010, 20, pp. 2157-2180.

