package com.times.jogadores.jogadores;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name="jogador")
public class Jogador {

	@Id
	@GeneratedValue(strategy = GenerationType.UUID)
	@Column(length=36)
	private String id;
	private String nome;
	private int idade;
	@Column(length=36)
	private String time_id;
	
	public Jogador() {
		
	}
	
	public Jogador(DadosCadastroJogador dados) {
		this.nome = dados.nome();
		this.idade = dados.idade();
		this.time_id = dados.time_id();
	}
	
	public String getId() {
		return id;
	}
	
	public void setId(String id) {
		this.id = id;
	}
	
	public String getNome() {
		return nome;
	}
	
	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public int getIdade() {
		return idade;
	}
	
	public void setIdade(int idade) {
		this.idade = idade;
	}
	
	public String getTime_id() {
		return time_id;
	}
	
	public void setTime_id(String time_id) {
		this.time_id = time_id;
	}
	
}
